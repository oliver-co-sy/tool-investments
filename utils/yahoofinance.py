from collections import namedtuple
from datetime import datetime
import yfinance as yf

StockData = namedtuple(
    "StockData", [
        "symbol",
        "long_name",
        "ex_dividend_date",
        "last_dividend_payment_date",
        "last_dividend_amount",
        "dividend_frequency",
        "fifty_two_week_low",
        "fifty_two_week_high",
        "trailing_pe",
        "forward_pe",
        "trailing_eps",
        "forward_eps",
        "book_value",
        "price_to_book_ratio",
        "price_target_mean",
        "price_target_median",
        "analyst_recommendation"
    ]
)


def get_stock_data(symbols):
    return [
        StockData(_get(ticker.info, "symbol"),
                  _get(ticker.info, "longName"),
                  _get(ticker.info, "exDividendDate", converter=datetime.fromtimestamp),
                  _get(ticker.info, "lastDividendDate", converter=datetime.fromtimestamp),
                  _get(ticker.info, "lastDividendValue"),
                  4,
                  _get(ticker.info, "fiftyTwoWeekLow"),
                  _get(ticker.info, "fiftyTwoWeekHigh"),
                  _get(ticker.info, "trailingPE"),
                  _get(ticker.info, "forwardPE"),
                  _get(ticker.info, "trailingEps"),
                  _get(ticker.info, "forwardEps"),
                  _get(ticker.info, "bookValue"),
                  _get(ticker.info, "priceToBook"),
                  _get(ticker.info, "targetMeanPrice"),
                  _get(ticker.info, "targetMedianPrice"),
                  _get(ticker.info, "recommendationKey"))
        for ticker in yf.Tickers(" ".join(symbols)).tickers.values()
    ]


def _get(dictionary, key, converter=None, default=None):
    try:
        value = dictionary[key]
        if converter is not None:
            return converter(value)
        return value
    except KeyError as e:
        return default
