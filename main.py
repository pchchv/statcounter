import os
from datetime import date
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from pymongo import MongoClient


app = FastAPI()
load_dotenv('.env')
client = MongoClient(os.getenv('MONGO'))
db = client['ststdb']
stat = db.stat

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
    doc = {
        "date": date.isoformat(),
        "views": views,
        "clicks": clicks,
        "cost": cost,
        "cpc": float('{:.2f}'.format(cost/clicks)),
        "cpm": float('{:.2f}'.format(cost/views*1000))
    }
    stat.insert_one(doc).inserted_id
    return {"status": "ok"}
