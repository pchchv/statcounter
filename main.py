from datetime import date
import os
import pprint
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from pymongo import MongoClient


app = FastAPI()
load_dotenv('.env')
client = MongoClient(os.getenv('MONGO'))
db = client['statsdb']
stats = db.stats


class Item(BaseModel):
    date: date
    views: int
    clicks: int
    cost: float


@app.get('/')
async def root():
    return {'message': 'Statistics counter service. Version 0.0.1', "status": "ok"}

@app.post('/')
async def read_item(date: date, views: int, clicks: int, cost: float):
    id = doc_loader(date, views, clicks, cost)
    return {"inserted_id": str(id), "status": "ok"}

@app.post('/json')
async def read_item(item: Item):
    id = doc_loader(item.date, item.views, item.clicks, item.cost)
    return {"inserted_id": str(id), "status": "ok"}


def doc_loader(date: date, views: int, clicks: int, cost: float):
    doc = {
        "date": date.isoformat(),
        "views": views,
        "clicks": clicks,
        "cost": cost,
        "cpc": float('{:.2f}'.format(cost/clicks)),
        "cpm": float('{:.2f}'.format(cost/views*1000))
    }
    return stats.insert_one(doc).inserted_id
