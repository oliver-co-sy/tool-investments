from argparse import ArgumentParser
from datetime import datetime

from utils import StockData, GoogleSheets, get_stock_data

parser = ArgumentParser(
    prog="stockloader.py",
    description="Retrieves data for the specified stock symbols and loads them to Google Sheets"
)

parser.add_argument(
    "-s",
    "--symbols",
    required=True,
    nargs="+",
    help="Stock symbols to load"
)

parser.add_argument(
    "-t",
    "--title",
    required=True,
    help="Title of the Google Sheets to load the stock data to"
)

args = parser.parse_args()

print(f"Retrieving data for stock symbols - {args.symbols} ...")
stock_data = get_stock_data(args.symbols)

print(f"Loading stock data to Google Sheets ...")
sheet = GoogleSheets(
    title=args.title,
    service_account_json_file="key.json"
)
sheet.set_headers(list(StockData._fields))
sheet.set_records([
    [
        column if not isinstance(column, datetime) else column.strftime("%d-%b-%Y")
        for column in row
    ]
    for row in stock_data
])

print(f"Stock data loaded successfully to {args.title}")
