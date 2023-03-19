from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import time
import random

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def read_root():
    aleatorio = random.randint(1, 10)
    time.sleep(aleatorio)
    r = requests.get('https://dummyjson.com/products/', )
    r.status_code
    products = r.json()
    return products['products']

@app.get("/carts")
def read_root():
    aleatorio = random.randint(1, 10)
    time.sleep(aleatorio)
    r = requests.get('https://dummyjson.com/carts/', )
    r.status_code
    products = r.json()
    return products['carts']

@app.get("/users")
def read_root():
    aleatorio = random.randint(1, 10)
    time.sleep(aleatorio)
    r = requests.get('https://dummyjson.com/users/', )
    r.status_code
    products = r.json()
    return products['users']

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
