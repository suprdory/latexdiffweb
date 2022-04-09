# import json
# from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
class Item(BaseModel):
    oldtex: str
    newtex: str

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
async def latexdiff(item:Item):
    
    f = open("old.tex", "w+")
    f.write(item.oldtex)
    f.close()
    f = open("new.tex", "w+")
    f.write(item.newtex)
    f.close()

    difftex = subprocess.run(["latexdiff", "old.tex", "new.tex"], \
        stdout=subprocess.PIPE).stdout.decode('utf-8')
    out = {'text': difftex}
    print(out)
    return out