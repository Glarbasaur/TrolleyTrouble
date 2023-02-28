from typing import Union

import uvicorn as uvicorn
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles


class Item(BaseModel):
    title: str
    # image: Image.new('RGB', (700, 400))
    description: str


app = FastAPI(static_folder='static')

templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")
response_class = HTMLResponse

Problem_Title = ["Classic", "Direct Action", "Indirect Action", "Is This Just Math", "Freedom of choice"]
Image_URL = ["heh.jpeg", "griffield.jfif", "woah haha.jpg", "sonicwar.jpg", "watchout.jpg"]
Problem_Text = [
    "A trolley is headed towards 5 people tied to the track. You can pull a lever to switch the trolley to a track where 1 person is tied.",
    "A trolley is headed towards 5 people tied to the track. You a large man is standing in front of you on a bridge. You can push the man onto the track to stop the trolley in time to save the 5.",
    "A trolley is headed towards 5 people tied to the track. You can pull the lever to switch the trolley to a track where you are tied.",
    "A trolley carrying 10 people is headed towards 5 people tied to the track. You can push a fat man onto the track, but you don’t know if the collision will de-rail the trolley, killing him and the passengers, or stop the trolley safely, killing only him.",
    "A trolley is headed towards 5 people who are standing on the track, waiting to be hit. You can pull the lever to switch the trolley to a track where 1 person is unwillingly tied. "]


def nextpage(k):
    k = k + 1
    return k


@app.get("/")
async def read_form():
    return "ghoooooosts"


@app.get("/{item_id}/")
def I_Have_No_Idea_What_Im_Doing(request: Request, item_id: int):
    response = templates.TemplateResponse('TrolleyTrouble.html', context={
        'request': request, 'ProblemTitle': Problem_Title[item_id], 'ImageURL': Image_URL[item_id],
        'ProblemText': Problem_Text[item_id], 'PageNumber': item_id, 'StaticLocation': '/static/styles.css'})
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
