from utils import GoogleSheetsFormulaGenerator

_HEADERS = ("Stock Symbol", "Current Price", "Dividend", "Frequency", "Dividend Yield")

formula_generator = GoogleSheetsFormulaGenerator(_HEADERS)

print(formula_generator.google_finance("TD.TO"))
print(formula_generator.multiply("Dividend", "Frequency", 1, 3))
print(formula_generator.percentage("Dividend", "Current Price", 1, 3))
