############################################################################################
# - data fetcher is responsible for appending data source at the end of each ID
############################################################################################

############################################################################################
# STOCK
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
# ETF
############################################################################################

### id ###
# etf id   : instrument.etf.<ticker>.<exchange>

### etf info ###
# isin     : instrument.etf.<ticker>.<exchange>.isin
# name     : instrument.etf.<ticker>.<exchange>.name
# currency : instrument.etf.<ticker>.<exchange>.currency

### etf market data (dependant on date) ###
# price    : instrument.etf.<ticker>.<exchange>.price.<date>

from abc import ABC, abstractmethod

from strenum import StrEnum


class DataType(StrEnum):
    INSTRUMENT_STOCK = "instrument.stock"
    INSTRUMENT_BOND = "instrument.bond"
    INSTRUMENT_ETF = "instrument.etf"
    INSTRUMENT_ETC = "instrument.etc"


class DataId(ABC):
    def uid(self) -> str:
        return f"{self._inner_type()}.{self._inner_uid()}"

    def __str__(self) -> str:
        return self.uid()

    @abstractmethod
    def _inner_type(self) -> DataType:
        pass

    @abstractmethod
    def _inner_uid(self) -> str:
        pass


############# BRAINSTORMING

# instrument.stock.aapl:us.nyse
# instrument.stock.aapl:us.nyse.isin@atlasetf
# instrument.stock.aapl:us.nyse.name@atlasetf
# instrument.stock.aapl:us.nyse.currency@atlasetf
# instrument.stock.aapl:us.nyse.price.2022-07-15@stooq
# instrument.stock.aapl:us.nyse.price.2005-03-04@yahoo
# economy.inflation.poland.yoy.2023.09.16@nbp
# economy.inflation.poland.mom.2020.02.07@nbp
# economy.unemployment.usa.yoy
# economy.unemployment.usa.yoy.1999.01.01@bloomberg
# instrument.etf.euna:de.xetra
# instrument.etf.euna:de.xetra.issuer
# instrument.etf.euna:de.xetra.issuer@atlasetf
# instrument.etf.euna:de.xetra.price.2000.08.08@google
