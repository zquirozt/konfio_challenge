from fastapi import FastAPI

from app.enums import Coin, Currency
from app.gecko_service import fetch_prices
from app.load_csv_postgres import load_csv
from app.write_csv_service import write_csv

app = FastAPI()


@app.get("/ping")
def read_root():
    return {"Hello": "World"}


@app.post("/bulk")
def read_root():
    result = fetch_prices(Coin.BITCOIN, Currency.DOLLAR, 1640996000, 1648706400)
    write_csv(result)
    load_csv()
    return {"Message": "Success bulk"}
