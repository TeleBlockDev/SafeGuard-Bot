🛡️ SafeGuard Bot
Intelligent Telegram Agent for Risk-Managed Crypto Insights
SafeGuard Bot is an AI-powered Telegram assistant that helps users monitor cryptocurrency markets through sentiment analysis, market intelligence, and risk-aware trading insights.

Built for the SoSoValue Buildathon, SafeGuard Bot combines institutional sentiment, real-time market data, and risk management principles into a simple Telegram experience.

🎯 Project Vision
Crypto markets move fast and are often driven by emotion. SafeGuard Bot helps users make more informed decisions by providing:

Real-time market intelligence

Sentiment-based insights

Risk-managed trade suggestions

Structured analysis instead of market noise

💡 Why SafeGuard Bot?
Most trading tools only display raw market data. SafeGuard Bot transforms data into actionable intelligence through:

Institutional sentiment analysis


Fear & Greed monitoring

Multi-source market pricing

Risk management guidance

Strategy recommendations

Mock trade simulation

🏗️ Architecture

Intelligence Layer

SoSoValue API (Primary)

Alternative.me Fear & Greed Index

CoinGecko Market Data

DefiLlama Yield Data

Analysis Engine

Async Python processing

Sentiment interpretation

Risk scoring logic

Strategy recommendation system

Delivery Layer

Telegram Bot Interface

Interactive button-driven navigation

Mobile-first user experience

🛠️ Tech Stack

Python

python-telegram-bot

AsyncIO

HTTPX

SQLite

SoSoValue API

CoinGecko API

Alternative.me API

DefiLlama API

SoDEX Testnet (Mock EIP-712 execution)

JustRunMy.App Hosting

🚀 Features

📊 Market Analysis

BTC, ETH, SOL, BNB, XRP & DOGE analysis

Live market prices

24-hour price change

Market overview dashboard

🧠 Sentiment Intelligence

SoSoValue institutional sentiment

Fear & Greed Index integration

Multi-factor SSI (SafeGuard Sentiment Index)

Opportunity detection

Strategy suggestions

🛡️ Risk Management

Maximum risk controls

Volatility awareness

Human confirmation workflow

Risk insights

💼 Portfolio & Trade History

Persistent SQLite storage

Portfolio tracking

Trade history

PnL analytics

Hit-rate calculation

🚀 Signal Generator

Entry price

Take-profit (TP)

Stop-loss (SL)

Risk/Reward ratio

Confidence score

💰 Live Yield Opportunities

Real-time DeFi yield opportunities

Powered by DefiLlam
a
🐳 Whale Monitoring

Whale activity dashboard

Large inflow/outflow insights

🔔 Smart Alerts

Fear & Greed alerts

Large BTC movement alerts

SSI threshold alerts

Whale activity notifications

🔄 Mock Trading

Simulated trade execution

SoDEX EIP-712 signing simulation

Testnet-style workflow

No real funds involved

⚙️ Reliability

API fallback system

Concurrent async API fetching

Error handling and recovery

Responsive Telegram UX

📊 Example Report

🛡️ SafeGuard Report — BTC

Price: $72,160
24h Change: -2.26%

Fear & Greed: 29 (Fear)

SSI Score: 74/100 (Bullish)

Signal:

🟢 Extreme Fear → Potential Opportunity

Strategy Suggestion:

Consider scaling into positions gradually.

Risk Insight:
Markets remain volatile.
Use proper position sizing and confirmations.

📦 Installation

Bash
git clone https://github.com/TeleBlockDev/SafeGuard-Bot.git

cd SafeGuard-Bot

pip install -r requirements.txt

python main.py

🔐 Environment Variables

Create a .env file:
Environment
BOT_TOKEN=your_telegram_bot_token

SOSO_API_KEY=your_sosovalue_api_key

🌊 Development Roadmap

✅ Wave 1
Telegram bot foundation
Multi-source pricing
BTC, ETH, SOL & BNB support
Fear & Greed integration

✅ Wave 2
Risk management system
Strategy engine
Interactive navigation
Improved reporting
Mock trade execution

✅ Wave 3
Advanced sentiment scoring
Portfolio tracking
Trade history
Whale activity monitoring
Automated alerts
Enhanced market intelligence

🚧 Wave 4
Live SoDEX integration
On-chain execution workflows
Advanced analytics dashboard
Wallet connectivity
Expanded DeFi opportunities

⚠️ Disclaimer
This project is for educational and demonstration purposes only.
Nothing provided by SafeGuard Bot should be considered financial advice. Always conduct your own research before making investment decisions.

🔗 Links
Telegram Bot
https://t.me/SafeGuardFiBot

GitHub Repository
https://github.com/TeleBlockDev/SafeGuard-Bot

YouTube Demo

https://www.youtube.com/watch?v=D7XO71I2nYc

👨‍💻 Built by TeleBlockDev
Built for the SoSoValue Buildathon.
