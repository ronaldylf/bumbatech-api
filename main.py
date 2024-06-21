from fastapi import FastAPI
import uvicorn
from users.routers import user_router

app = FastAPI()

@app.get('/')
def home():
    return "Hello world"

app.include_router(user_router.router)

if __name__ == '__main__':
    uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=8000,
    reload=True, # remove this after tests
    workers=1 # remove this after tests
    )