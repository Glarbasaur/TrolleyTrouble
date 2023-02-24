from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image

class Item(BaseModel):
    title: str
    #image: Image.new('RGB', (700, 400))
    description: str





app = FastAPI()

@app.get("/")
async def root():
    return {"message": "http:trolleytrouble.fun"}

# @app.put("/", )
