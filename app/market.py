import yfinance as yf
from datetime import datetime


def get_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1m")

        if data.empty:
            return None

        return round(float(data["Close"].iloc[-1]), 2)

    except Exception:
        return None


def market_snapshot():

    return {
        "timestamp": datetime.utcnow().isoformat(),

        "gold": get_price("GC=F"),
        "silver": get_price("SI=F"),

        "brent": get_price("BZ=F"),
        "wti": get_price("CL=F"),

        "bitcoin": get_price("BTC-USD"),
        "ethereum": get_price("ETH-USD"),

        "eurusd": get_price("EURUSD=X"),

        "dxy": get_price("DX-Y.NYB"),

        "vix": get_price("^VIX")
    }
