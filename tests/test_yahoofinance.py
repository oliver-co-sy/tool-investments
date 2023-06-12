from utils import get_stock_data, GoogleFinanceFieldFormatter

stock_data = get_stock_data(
    symbols=[
        "TD.TO",
        "RY.TO",
        "BMO.TO"
    ], formatter_cls=GoogleFinanceFieldFormatter)
print(stock_data)

stock_data = get_stock_data(
    symbols=[
        "SRV-UN.TO"
    ], formatter_cls=GoogleFinanceFieldFormatter)
print(stock_data)
