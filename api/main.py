import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
# import pytemplog
app = FastAPI()

origins = [
    # "http://192.168.1.200:8000",
    "https://suprdory.github.io",
    "http://127.0.0.1:5500",
    # "http://192.168.1.230"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/latexdiff")
async def latexdiff(data):
    difftex = "test nonsense"
    return difftex

# @app.get("/dict")
# async def todict():
#     templog_dict=pytemplog.combine2dict()
#     return templog_dict

# @app.get("/")
# async def root():
#     return {"message": "Test success"}