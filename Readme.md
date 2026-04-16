# Binance Futures Trading Bot (Testnet)

## Overview

A simple CLI-based trading bot built in Python that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).
The project demonstrates clean architecture, input validation, logging, and error handling.

---

## Features

* Place **MARKET** and **LIMIT** orders
* Supports **BUY** and **SELL**
* CLI-based input using Typer
* Input validation using Pydantic
* Logging of requests, responses, and errors
* Structured and modular codebase

---

## Tech Stack

* Python 3.x
* httpx (HTTP client)
* Typer (CLI)
* Pydantic (validation)
* python-dotenv (environment variables)

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd trading_bot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.01 --price 30000
```

---

## Example Output

```json
{
  "orderId": 123456789,
  "status": "FILLED",
  "executedQty": "0.01",
  "avgPrice": "64000.12"
}
```

---

## Logs

All API requests, responses, and errors are logged to:

```
logs/trading.log
```

---

## Assumptions

* Only Binance Futures Testnet is used
* API keys are valid and active
* User provides correct symbol and quantity precision

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Notes

* Ensure system time is synced to avoid timestamp errors
* Use valid quantity precision based on Binance rules
* This project is for testnet use only (not production trading)
