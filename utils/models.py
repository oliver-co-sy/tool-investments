from collections import namedtuple

StockData = namedtuple(
    "StockData", [
        "symbol",
        "long_name",
        "current_price",
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
