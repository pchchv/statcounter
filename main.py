from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Statistics counter service. Version 0.0.1', "status": "ok"}