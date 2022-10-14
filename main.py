import os
from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient


app = FastAPI()
load_dotenv('.env')
client = MongoClient(os.getenv('MONGO'))
db = client['links-database']
links = db.links


@app.get('/')
async def root():
    return {'message': 'Statistics counter service. Version 0.0.1', "status": "ok"}