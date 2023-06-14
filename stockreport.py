from argparse import ArgumentParser
from services import NewReport

parser = ArgumentParser(
    prog="stockreport.py",
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

parser.add_argument(
    "-e",
    "--email",
    required=True,
    help="The email to share the Google Sheets with"
)

args = parser.parse_args()
NewReport(title=args.title, symbols=args.symbols, email=args.email).generate()
