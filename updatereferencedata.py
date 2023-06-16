from argparse import ArgumentParser
from services import UpdateStockReference

parser = ArgumentParser(
    prog="updatereferencedata.py",
    description="Updates the data in the Investments spreadsheet reference worksheet"
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

parser.add_argument(
    "-w",
    "--worksheet",
    required=True,
    help="Title of the worksheet to update"
)

args = parser.parse_args()
UpdateStockReference(
    title=args.title,
    worksheet=args.worksheet,
    symbols=args.symbols
).generate()
