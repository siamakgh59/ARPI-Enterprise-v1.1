import yfinance as yf
from datetime import datetime


def get_market_data(symbol):

    try:
        ticker = yf.Ticker(symbol)

        data = ticker.history(
            period="2d",
            interval="1m"
        )

        if data.empty:
            return {
                "price": None,
                "change": None,
                "status": "NO_DATA"
            }

        price = float(data["Close"].iloc[-1])

        previous = float(data["Close"].iloc[0])

        change = ((price - previous) / previous) * 100

        return {
            "price": round(price,2),
            "change_percent": round(change,2),
            "status": "LIVE"
        }


    except Exception:

        return {
            "price": None,
            "change_percent": None,
            "status": "ERROR"
        }



def market_snapshot():

    return {

        "timestamp":
        datetime.utcnow().isoformat(),

        "gold":
        get_market_data("GC=F"),

        "silver":
        get_market_data("SI=F"),

        "brent":
        get_market_data("BZ=F"),

        "wti":
        get_market_data("CL=F"),

        "bitcoin":
        get_market_data("BTC-USD"),

        "ethereum":
        get_market_data("ETH-USD"),

        "eurusd":
        get_market_data("EURUSD=X"),

        "dxy":
        get_market_data("DX-Y.NYB"),

        "vix":
        get_market_data("^VIX")
    }
