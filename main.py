from typing import Union

import uvicorn as uvicorn
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles


class Item(BaseModel):
    title: str
    #image: Image.new('RGB', (700, 400))
    description: str

app = FastAPI()

templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")
response_class=HTMLResponse

Problem_Title = ["Classic", "Direct Action", "Indirect Action", "Is This Just Math", "Freedom of choice"]
Image_URL = ["heh.jpeg", "griffield.jfif", "woah haha.jpg", "sonicwar.jpg", "watchout.jpg"]
Problem_Text =["A trolley is headed towards 5 people tied to the track. You can pull a lever to switch the trolley to a track where 1 person is tied.",
               "A trolley is headed towards 5 people tied to the track. You a large man is standing in front of you on a bridge. You can push the man onto the track to stop the trolley in time to save the 5.",
               "A trolley is headed towards 5 people tied to the track. You can pull the lever to switch the trolley to a track where you are tied.",
               "A trolley carrying 10 people is headed towards 5 people tied to the track. You can push a fat man onto the track, but you don’t know if the collision will de-rail the trolley, killing him and the passengers, or stop the trolley safely, killing only him.",
               "A trolley is headed towards 5 people who are standing on the track, waiting to be hit. You can pull the lever to switch the trolley to a track where 1 person is unwillingly tied. "]

n=0

def nextpage(k):
    k=k+1
    return k

@app.get("/")
async def read_form():
    return "ghoooooosts"



@app.get("/funny")
def I_Have_No_Idea_What_Im_Doing(request: Request):
    global n
    response = templates.TemplateResponse('TrolleyTrouble.html', context={
        'request': request, 'ProblemTitle': Problem_Title[n], 'ImageURL': Image_URL[n], 'ProblemText': Problem_Text[n]})
    n += 1
    return response

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return int({"item_id": item_id})+1, I_Have_No_Idea_What_Im_Doing()


# @app.get("/funny")
# def onclick(request: Request, num: int= n, action: str = Form(...)):
#     if action == 'Watch':
#         nextpage(n)
#         I_Have_No_Idea_What_Im_Doing()
#     if action == 'Lever':
#         nextpage(n)
#         I_Have_No_Idea_What_Im_Doing()
#         uvicorn.run("main:app", reload=True)
#

# @app.get("/funny")
# def button_press():
#     n= n+1

# @app.post("/form")
# def maybesomethingnew(request: Request):
#
#     return templates.TemplateResponse('TrolleyTrouble.html', context={'request': request, 'result': result})



# @app.put("/", )


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)