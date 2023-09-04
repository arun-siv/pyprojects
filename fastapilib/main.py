from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return {"message": "Hello world"}

@app.get('/notes')
async def get_all_notes():
    pass
