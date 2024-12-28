from fastapi import FastAPI
import uvicorn, datetime


from graphql_api.config import settings

print ("dbg 1 --->")
'''
from src.graphql_api import graphql_app

app = FastAPI()
app.mount ('/graph', graphql_app)


@app.on_event ('startup')
async def startup():
    public_paths = {'/', '/graph/'},

@app.get ("/")
async def root():
    return {"message": {
        "app_mame": settings.APP_NAME,
        "system_time": datetime.datetime.now()
    }}

if __name__ == "__main__":
    uvicorn.run (
        "main:app",
        host=settings.HOST,
        reload=True,
        port=settings.PORT,
        debug = False
    )
'''

'''
app = FastAPI()

@app.get("/")

async def root():
    return {"mesage": "Hello Mundo"}

'''