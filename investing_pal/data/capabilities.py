from dataclasses import dataclass

from data.value import DataType
from instruments.securities.equity.stock import StockId


@dataclass
class Capability:
    data_id: str
    data_type: DataType


# Stocks.
stock_name = Capability(f"{StockId.uid_format()}.name", DataType.TEXT)
stock_isin = Capability(f"{StockId.uid_format()}.isin", DataType.TEXT)
stock_currency = Capability(f"{StockId.uid_format()}.currency", DataType.TEXT)
stock_price = Capability(f"{StockId.uid_format()}.price", DataType.PRICE)
