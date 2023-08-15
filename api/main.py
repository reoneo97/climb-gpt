from typing import Union

from fastapi import FastAPI
from app.posts import router as posts_router
from fastapi.middleware.cors import CORSMiddleware
from app.config import AppConfig

app = FastAPI()

origins = [

    "http://localhost/*",
    "http://localhost:3000/",
    "http://localhost:3000",

]
app = FastAPI()
app.include_router(posts_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    print('Working')
    return {"Hello again does this work": "World"}


@app.get("/path")
def test():
    return {"path": AppConfig.segment.checkpoint}