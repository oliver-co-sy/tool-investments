from abc import ABC, abstractmethod

from utils import \
    GoogleSheets, \
    GoogleSheetsFormulaGenerator, \
    get_stock_data, \
    log


class Report(ABC):
    def __init__(self, title, symbols, headers):
        self._title = title
        self._symbols = symbols
        self._headers = headers
        self._formula_generator = GoogleSheetsFormulaGenerator(self._headers)

    def generate(self):
        log(f"Retrieving stock data for {self._symbols}...")
        stock_data = get_stock_data(self._symbols)

        log(f"Writing stock data to Google Sheets ({self._title})...")
        spreadsheet = self.create_spreadsheet()
        spreadsheet.set_headers(self._headers)
        spreadsheet.set_records(self.map_data(stock_data))

        log(f"Stock data saved successfully")

    @abstractmethod
    def create_spreadsheet(self):
        return GoogleSheets(service_account_json_file="key.json")

    @abstractmethod
    def map_data(self, stock_data):
        pass


class NewReport(Report):
    _HEADERS = (
        "Symbol",
        "Name",
        "Price",
        "Ex-Dividend Date",
        "Last Dividend Payment",
        "Last Dividend Amount",
        "Dividend Frequency",
        "52-Week Low",
        "52-Week High",
        "Trailing PE",
        "Forward PE",
        "Trailing EPS",
        "Forward EPS",
        "Book Value",
        "Price-to-Book",
        "Price Target Mean",
        "Price Target Median",
        "Recommendation"
    )

    def __init__(self, title, symbols, email):
        super().__init__(title, symbols, self._HEADERS)
        self._email = email

    def create_spreadsheet(self):
        spreadsheet = super().create_spreadsheet()
        spreadsheet.new(
            title=self._title,
            email=self._email
        )
        return spreadsheet

    def map_data(self, stock_data):
        return [
            [
                record.symbol,
                record.long_name,
                self._formula_generator.google_finance(record.symbol),
                record.ex_dividend_date.strftime("%d-%b-%Y") if record.ex_dividend_date else None,
                record.last_dividend_payment_date.strftime("%d-%b-%Y") if record.last_dividend_payment_date else None,
                record.last_dividend_amount,
                record.dividend_frequency,
                record.fifty_two_week_low,
                record.fifty_two_week_high,
                record.trailing_pe,
                record.forward_pe,
                record.trailing_eps,
                record.forward_eps,
                record.book_value,
                record.price_to_book_ratio,
                record.price_target_mean,
                record.price_target_median,
                record.analyst_recommendation
            ]
            for record in stock_data
        ]


class UpdateStockReference(Report):
    _HEADERS = (
        "Stock Symbol",
        "Current Price",
        "Dividend",
        "Frequency",
        "Annual Dividend",
        "Dividend Yield",
        "Ex-Dividend Date",
        "Payable Date"
    )

    def __init__(self, title, symbols):
        super().__init__(title, symbols, self._HEADERS)

    def create_spreadsheet(self):
        spreadsheet = super().create_spreadsheet()
        spreadsheet.open(self._title)
        return spreadsheet

    def map_data(self, stock_data):
        return [
            [
                record.symbol,
                self._formula_generator.google_finance(
                    stock_symbol=record.symbol
                ),
                record.last_dividend_amount,
                record.dividend_frequency,
                self._formula_generator.multiply(
                    field_name_1="Dividend",
                    field_name_2="Frequency",
                    field_row=index + 1
                ),
                self._formula_generator.percentage(
                    field_name_1="Annual Dividend",
                    field_name_2="Current Price",
                    field_row=index + 1
                ),
                record.ex_dividend_date.strftime("%d-%b-%Y") if record.ex_dividend_date else None,
                record.last_dividend_payment_date.strftime("%d-%b-%Y") if record.last_dividend_payment_date else None
            ]
            for index, record in enumerate(stock_data)
        ]
