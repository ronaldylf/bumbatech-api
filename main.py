from fastapi import FastAPI
#import uvicorn
from users.routers import user_router

app = FastAPI(
    title="BumbatechAPI",
    description="Documentação da api da Bumbatech"
)

@app.get('/')
def home():
    return "Bumbatech"

app.include_router(user_router.router)

'''
if __name__ == '__main__':
    uvicorn.run(
    "main:app",
    port=8001,
    reload=True,
    workers=1
    )
'''