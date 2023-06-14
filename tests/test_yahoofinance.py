from utils import get_stock_data

stock_data = get_stock_data(
    symbols=[
        "TD.TO",
        "RY.TO",
        "BMO.TO"
    ]
)
print(stock_data)

stock_data = get_stock_data(
    symbols=[
        "SRV-UN.TO"
    ]
)
print(stock_data)
