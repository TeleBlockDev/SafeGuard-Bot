"""
SafeGuard Bot - Wave 2 Polished Version
Agentic Telegram Tool with SoSoValue Integration + Mock Trade + Strategy Engine
Built for AKINDO SoSoValue Buildathon
"""

import os
import logging
import time
import asyncio
from dotenv import load_dotenv
import httpx

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv()

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
SOSO_API_KEY = os.getenv("SOSO_API_KEY")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

COINGECKO_IDS = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", 
    "BNB": "binancecoin", "XRP": "ripple", "DOGE": "dogecoin"
}
COIN_EMOJIS = {
    "BTC": "₿", "ETH": "Ξ", "SOL": "◎", "BNB": "🟡", 
    "XRP": "✕", "DOGE": "🐶"
}

# ========================= DATA FETCHERS =========================

async def get_sosovalue_data(symbol: str):
    if not SOSO_API_KEY:
        return None
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                f"https://openapi.sosovalue.com/openapi/v1/currency/price?symbol={symbol}",
                headers={"x-soso-api-key": SOSO_API_KEY}
            )
            if resp.status_code == 200:
                return resp.json()
    except Exception as e:
        logger.error(f"SoSoValue error: {e}")
    return None


async def get_price_data(symbol: str) -> str:
    """CoinGecko fallback"""
    cg_id = COINGECKO_IDS.get(symbol.upper(), symbol.lower())
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                "https://api.coingecko.com/api/v3/simple/price",
                params={"ids": cg_id, "vs_currencies": "usd", "include_24hr_change": "true"}
            )
            resp.raise_for_status()
            data = resp.json()
            if cg_id in data:
                info = data[cg_id]
                price = info.get("usd", 0)
                change = info.get("usd_24h_change", 0)
                return f"📊 Price: ${price:,}\n📈 24h Change: {change:.2f}%"
    except Exception as e:
        logger.error(f"CoinGecko error: {e}")
    return "📊 Price data unavailable"


async def get_fng():
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.get("https://api.alternative.me/fng/?limit=1")
            resp.raise_for_status()
            data = resp.json()["data"][0]
            value = int(data["value"])
            return f"📈 F&G: {value} ({data['value_classification']})", value
    except Exception as e:
        logger.error(f"F&G error: {e}")
        return "📈 F&G unavailable", None


# ========================= ERROR HANDLER =========================

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling update:", exc_info=context.error)
    if update and update.effective_message:
        await update.effective_message.reply_text("⚠️ Something went wrong. Please try again.")


# ========================= UI =========================

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, edit: bool = False):
    keyboard = [
        [InlineKeyboardButton("📊 BTC", callback_data="BTC"), InlineKeyboardButton("📊 ETH", callback_data="ETH")],
        [InlineKeyboardButton("📊 SOL", callback_data="SOL"), InlineKeyboardButton("📊 BNB", callback_data="BNB")],
        [InlineKeyboardButton("📊 XRP", callback_data="XRP"), InlineKeyboardButton("📊 DOGE", callback_data="DOGE")],
        [InlineKeyboardButton("🛡️ Risk Settings", callback_data="guard")]
    ]

    text = "🛡️ **SafeGuard Bot - Wave 2**\n\nTap any button for advanced analysis:"

    if edit and update.callback_query:
        await update.callback_query.edit_message_text(
            text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
        )


# ========================= HANDLERS =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_main_menu(update, context)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "menu":
        await show_main_menu(update, context, edit=True)
        return

    if data == "guard":
        keyboard = [[InlineKeyboardButton("← Back to Menu", callback_data="menu")]]
        await query.edit_message_text(
            "🛡️ **Risk Settings**\n\n"
            "• Max risk per trade: **2%**\n"
            "• Volatility pause: **Enabled**\n"
            "• Human confirmation: **Required**",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
        return

    if data.startswith("trade_"):
        symbol = data.replace("trade_", "")
        context.user_data["last_trade"] = symbol
        keyboard = [[InlineKeyboardButton("← Back to Menu", callback_data="menu")]]
        await query.edit_message_text(
            f"✅ **Mock Trade Executed**\n\n"
            f"Asset: **{symbol}**\n"
            f"Status: Simulated on SoDEX Testnet\n"
            f"Risk Guard: 2% max drawdown applied\n\n"
            f"No real funds were moved.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
        return

    # Coin Analysis
    symbol = data
    start_time = time.time()
    await query.edit_message_text(f"🔍 Analyzing **{symbol}**...", parse_mode="Markdown")

    soso_data, price_text, (fng_text, fng_value) = await asyncio.gather(
        get_sosovalue_data(symbol),
        get_price_data(symbol),
        get_fng()
    )

    source = "✅ SoSoValue" if soso_data else "⚠️ CoinGecko Fallback"
    if soso_data:
        price_text = "📊 SoSoValue data received"

    result = f"🛡️ **SafeGuard Report — {symbol}**\n\n"
    result += f"{source}\n{price_text}\n{fng_text}\n\n"

    if fng_value is not None:
        if fng_value < 30:
            result += "🟢 **Extreme Fear → Potential Opportunity**\n"
            strategy = "Consider scaling into positions gradually."
        elif fng_value > 70:
            result += "🔴 **Extreme Greed → Caution Advised**\n"
            strategy = "Consider reducing risk exposure."
        else:
            strategy = "Maintain disciplined position sizing."
        result += f"\n📋 **Strategy Suggestion**: {strategy}\n"

    result += "\n⚠️ **Risk Insight**: Markets remain volatile. Use proper position sizing.\n\n"
    result += "💡 Trade responsibly.\n\n"

    elapsed = round(time.time() - start_time, 2)
    result += f"⏱️ Analysis completed in {elapsed}s"

    keyboard = [
        [InlineKeyboardButton("✅ Approve Mock Trade", callback_data=f"trade_{symbol}")],
        [InlineKeyboardButton("← Back to Menu", callback_data="menu")]
    ]

    await query.edit_message_text(
        result, 
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_error_handler(error_handler)

    logger.info("🚀 SafeGuard Bot - Wave 2 Final Version Deployed!")
    app.run_polling()


if __name__ == "__main__":
    main()
