import gspread


class GoogleSheets:
    def __init__(self, service_account_json_file="key.json"):
        self._client = gspread.service_account(service_account_json_file)
        self._spreadsheet = None
        self._worksheet = None

    def open(self, title):
        self._spreadsheet = self._client.open(title)
        self._worksheet = self._spreadsheet.sheet1

    def new(self, title, email):
        self._spreadsheet = self._client.create(title)
        self._spreadsheet.share(email_address=email, perm_type="user", role="writer")
        self._worksheet = self._spreadsheet.sheet1

    def select_worksheet(self, title):
        self._worksheet = self._spreadsheet.worksheet(title)

    def add_worksheet(self, title, rows=5, cols=5):
        self._worksheet = self._spreadsheet.add_worksheet(title, rows, cols)

    def delete_worksheet(self):
        if self._worksheet is self._spreadsheet.sheet1:
            raise RuntimeError("Cannot delete sheet 1")
        self._spreadsheet.del_worksheet(self._worksheet)
        self._worksheet = self._spreadsheet.sheet1

    def set_headers(self, headers=None):
        if not headers:
            raise ValueError("Headers are required")

        self._worksheet.update("A1:Z1", [headers])
        self._worksheet.format("A1:Z1", {
            "backgroundColor": {
                "red": 95,
                "green": 99,
                "blue": 104
            },
            "horizontalAlignment": "CENTER",
            "textFormat": {
                "foregroundColor": {
                    "red": 211,
                    "green": 211,
                    "blue": 211
                },
                "fontSize": 10,
                "bold": True
            }
        })

    def set_records(self, records):
        if not records:
            raise ValueError("Records are required")
        self._worksheet.update("A3", records, value_input_option="USER_ENTERED")

    def clear_records(self):
        self._worksheet.clear()


class GoogleSheetsFormulaGenerator:
    ROW_OFFSET = 2

    def __init__(self, headers):
        self._header_to_column = {
            header.lower(): chr(65 + index).upper()
            for index, header in enumerate(headers)
        }

    def google_finance(self, stock_symbol):
        symbol_tokens = self._tokenize_stock_symbol(stock_symbol)
        return f'=GOOGLEFINANCE("{symbol_tokens[2]}:{symbol_tokens[0]}", "price")'

    def multiply(self, field_name_1, field_name_2, field_row, round_=2):
        return f"=ROUND({self._cell(field_name_1, field_row)}*{self._cell(field_name_2, field_row)},{round_})"

    def percentage(self, field_name_1, field_name_2, field_row, round_=2):
        return f"=ROUND({self._cell(field_name_1, field_row)}/{self._cell(field_name_2, field_row)}*100,{round_})"

    def _cell(self, field_name, row):
        row += self.ROW_OFFSET
        column = self._header_to_column[field_name.lower()]
        return f"{column}{row}"

    @staticmethod
    def _tokenize_stock_symbol(stock_symbol):
        if "." in stock_symbol:
            index = stock_symbol.index(".")
            prefix = stock_symbol[:index]
            suffix = stock_symbol[index + 1:]
            if suffix.upper() == "TO":
                return prefix, suffix, "TSE"
        return stock_symbol, None, "NYSE"
