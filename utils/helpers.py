def tokenize_stock_symbol(stock_symbol):
    if "." in stock_symbol:
        index = stock_symbol.index(".")
        prefix = stock_symbol[:index]
        suffix = stock_symbol[index + 1:]
        if suffix.upper() == "TO":
            return prefix, suffix, "TSE"
    return stock_symbol, None, "NYSE"


def google_finance_price_formula(stock_symbol):
    symbol_tokens = tokenize_stock_symbol(stock_symbol)
    return f'=GOOGLEFINANCE("{symbol_tokens[2]}:{symbol_tokens[0]}", "price")'
