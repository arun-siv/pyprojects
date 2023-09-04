from fastapi import FastAPI
from uvicorn import run
from requests import get
from multiprocessing import Process

app = FastAPI()

@app.get('/test')
async def test():
    return {'success': True}

if __name__ == '__main__':
    def target():
        print(get('http://127.0.0.1:8000/test'))
    process = Process(target=target)
    process.start()
    run(app)
    process.join()
