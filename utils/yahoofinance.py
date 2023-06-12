import yfinance as yf
from datetime import datetime
from utils import DefaultFieldFormatter
from utils import StockData


def get_stock_data(symbols, formatter_cls=DefaultFieldFormatter):
    stock_data = []
    for ticker in yf.Tickers(" ".join(symbols)).tickers.values():
        field_formatter = formatter_cls(_get(ticker.info, "symbol"))
        stock_data.append(
            StockData(
                field_formatter.format("symbol", _get(ticker.info, "symbol")),
                field_formatter.format("long_name", _get(ticker.info, "longName")),
                field_formatter.format("current_price", _get(ticker.info, "currentPrice")),
                field_formatter.format("ex_dividend_date",
                                       _get(ticker.info, "exDividendDate", converter=datetime.fromtimestamp)),
                field_formatter.format("last_dividend_payment_date",
                                       _get(ticker.info, "lastDividendDate", converter=datetime.fromtimestamp)),
                field_formatter.format("last_dividend_amount", _get(ticker.info, "lastDividendValue")),
                4,
                field_formatter.format("fifty_two_week_low", _get(ticker.info, "fiftyTwoWeekLow")),
                field_formatter.format("fifty_two_week_high", _get(ticker.info, "fiftyTwoWeekHigh")),
                field_formatter.format("trailing_pe", _get(ticker.info, "trailingPE")),
                field_formatter.format("forward_pe", _get(ticker.info, "forwardPE")),
                field_formatter.format("trailing_eps", _get(ticker.info, "trailingEps")),
                field_formatter.format("forward_eps", _get(ticker.info, "forwardEps")),
                field_formatter.format("book_value", _get(ticker.info, "bookValue")),
                field_formatter.format("price_to_book_ratio", _get(ticker.info, "priceToBook")),
                field_formatter.format("price_target_mean", _get(ticker.info, "targetMeanPrice")),
                field_formatter.format("price_target_median", _get(ticker.info, "targetMedianPrice")),
                field_formatter.format("analyst_recommendation", _get(ticker.info, "recommendationKey"))
            )
        )
    return stock_data


def _get(dictionary, key, converter=None):
    try:
        value = dictionary[key]
        if converter is not None:
            return converter(value)
        return value
    except KeyError as e:
        return None
