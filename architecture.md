# Architecture

## Packages and modules

```plain
app/
    bond_calculator/
        api/
        main.py
        ui/

input/
    __init__.py
    data/
        fetcher.py (DataFetcher, IDataSource)
        sources/
            atlasetf.py
            stooq.py
            yahoo.py
        value.py (Number, Text, Price, Percentage)

output/
    __init__.py
    db.py
    plotter.py
```

- market simulator (simulate time on markets)
- taxes
- statistics
- data events
- strategies
- securities/
  - bond.py
  - etf.py
  - stock.py
- finances/
  - currency.py
- economy/
  - inflation.py
  - industry.py (UnemploymentRate)
- institutions/
  - bank/
    - poland/
      - mbank.py
      - millenium.py
  - broker/
    - poland/
      - bossa.py
      - xtb.py
- user/
  - manager.py
  - portfolio.py (Account)
