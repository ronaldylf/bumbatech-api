from fastapi import FastAPI, Depends
#import uvicorn
from users.routers import user_router

from autentication import scheme

app = FastAPI(
    title="BumbatechAPI",
    description="Documentação da api da Bumbatech"
)

@app.get('/')
def home():
    return "Bumbatech"

app.include_router(user_router.router, dependencies=[Depends(scheme.check_access_token)])

'''
if __name__ == '__main__':
    uvicorn.run(
    "main:app",
    port=8001,
    reload=True,
    workers=1
    )
'''