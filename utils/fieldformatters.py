class DefaultFieldFormatter:
    def __init__(self, symbol):
        self._symbol = symbol

    def format(self, field_name, field_value):
        if field_name in ("ex_dividend_date", "last_dividend_payment_date") and field_value:
            return field_value.strftime("%d-%b-%Y")
        return field_value


class GoogleFinanceFieldFormatter(DefaultFieldFormatter):
    def format(self, field_name, field_value):
        field_value = super().format(field_name, field_value)
        if field_name == "current_price" and field_value:
            symbol_tokens = self._tokenize()
            return f"=GOOGLEFINANCE('{symbol_tokens[2]}:{symbol_tokens[0]}', 'price')"
        return field_value

    def _tokenize(self):
        if "." in self._symbol:
            index = self._symbol.index(".")
            prefix = self._symbol[:index]
            suffix = self._symbol[index + 1:]
            if suffix.upper() == "TO":
                return prefix, suffix, "TSE"
        return self._symbol, None, "NYSE"
