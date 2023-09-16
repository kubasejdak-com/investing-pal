############################################################################################
# - data fetcher is responsible for appending data source at the end of each ID
############################################################################################

############################################################################################
# STOCKS
############################################################################################

### id ###
# stock id : instrument.stock.<ticker>.<exchange>

### stocks info ###
# isin     : instrument.stock.<ticker>.<exchange>.isin
# name     : instrument.stock.<ticker>.<exchange>.name
# currency : instrument.stock.<ticker>.<exchange>.currency

### stocks market data (dependant on date) ###
# price    : instrument.stock.<ticker>.<exchange>.price.<date>


############################################################################################
############################################################################################

from abc import ABC

from strenum import StrEnum


class DataType(StrEnum):
    INSTRUMENT_STOCK = "instrument.stock"
    INSTRUMENT_BOND = "instrument.bond"
    INSTRUMENT_ETF = "instrument.etf"
    INSTRUMENT_ETC = "instrument.etc"


class DataId(ABC):
    def __init__(self, type: DataType) -> None:
        self.type: DataType = type

    def __str__(self) -> str:
        return f"{self.type}"


############# BRAINSTORMING

# instrument.[stock|etf|etc].<ticker>.<source>
# instrument.[bond].<symbol>.price.<source>
# source.<source>
# economy.inflation.<country>.<period>

# economy.inflation.poland.yoy.nbp
