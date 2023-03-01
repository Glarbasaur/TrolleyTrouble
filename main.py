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

Problem_Title = ["Intro", "Classic", "Direct Action", "Responsibility", "Is This Just Math", "Freedom of choice",
                 "Intellectual Property", "Unknown Knowledge", "Unknown Scriptures", "Class Loyalties", "Educational",
                 "Redemption", "Lifespans", "Organic", "Judgement", "Immaturity", "Bribery", "How much?", "Uncertainty",
                 "The Poorly Lit Knight", "A Lotta Damage", "Testing for Homicide", "Double Checking",
                 "Testing for `Pathy", "Testing Values", "Death of Media", "Time Travel", "Patriotism"]
Image_URL = ["heh.jpeg", "griffield.jfif", "woah haha.jpg", "sonicwar.jpg", "watchout.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg", "woah haha.jpg"]
Problem_Text = [
    "This site was made as a practice project for entry with HTML. I was looking for example trolley problems and found the site 'https://neal.fun/absurd-trolley-problems/' by Neal. I had a number of other ideas for problems, and it seemed like a simple enough first project. Some problems are used from Neal's set.."
    "A trolley is headed towards 5 people tied to the track. You can pull a lever to switch the trolley to a track where 1 person is tied.",
    "A trolley is headed towards 5 people tied to the track. You a large man is standing in front of you on a bridge. You can push the man onto the track to stop the trolley in time to save the 5.",
    "A trolley is headed towards 5 people tied to the track. You can pull the lever to switch the trolley to a track where you are tied.",
    "A trolley carrying 10 people is headed towards 5 people tied to the track. You can push a fat man onto the track, but you don’t know if the collision will de-rail the trolley, killing him and the passengers, or stop the trolley safely, killing only him.",
    "A trolley is headed towards 5 people who are standing on the track, waiting to be hit. You can pull the lever to switch the trolley to a track where 1 person is unwillingly tied.",
    "A trolley is headed towards 5 people tied to the track. You can pull a lever to switch the trolley to a track where someone has left the original copy of a 4th century manuscript that has been scanned and digitized.",
    "A trolley is headed towards 5 people tied to the track. You can pull a lever to switch the trolley to a track where someone has left a newly discovered 4th century manuscript.",
    "A trolley is headed towards 5 people tied to the track. You can pull a lever to switch the trolley to a track where someone has left a box of newly discovered original scrolls of the early abrahamic religions",
    "A trolley is headed towards 1 poor janitor tied to the track. You can pull a lever to switch the trolley to a track where 1 wealthy stock-broker is tied.",
    "A trolley is headed towards 1 shelf restocker tied to the track. You can pull a lever to switch the trolley to a track where 1 acclaimed astrophysicist is tied."
    "A trolley is headed towards 5 convicted and released murderers. You can pull a lever to switch the trolley to a track where 1 person is tied who has never seriously hurt anyone in their life.",
    "A trolley is headed towards a track where 5 elderly people have been tied. You can pull a lever to switch the trolley to a track where 1 baby has been tied.",
    "A trolley is headed towards a track where 5 sentient robots, capable of feeling pain, have been tied. You can pull a lever to switch the trolley to a track where 1 human has been tied.",
    "A trolley is headed towards a track where 1 well liked, kind person is tied. You can pull a lever to switch the trolley to a track where 1 disliked, rude person is tied.",
    "A trolley is headed towards a track where 1 obedient child is tied. You can pull a lever to switch the trolley to a track where 1 disobedient child is tied.",
    "A trolley is headed towards a track where 1 person is tied. They offer you 100,000 USD to pull a lever to switch the trolley to a track where 1 person is tied.",
    "A trolley is headed towards a track where 1 person is tied. They offer you 500,000,000 USD to pull a lever to switch the trolley to a track where 5 people are tied.",
    "A trolley is headed towards a track where 1 person is tied. You can pull a lever, but you don’t know what will happen. Will it slow the trolley down and make their death more painful? Speed it up and make it less painful? Switch to a track where 3,000 people and an undiscovered holy manuscript are laying? Or stop the trolley?",
    "A trolley is headed towards a track where the person you love most is tied. You can pull a lever to switch the trolley to a track where a prominent politician.",
    "A trolley is headed towards a track where 1 person is tied. You can pull a lever to switch the trolley to a track where 5 people’s legs are tied onto a track, where the trolley will sever them entirely",
    "A trolley is headed towards a track where 1 person is tied. You owe them 600,000 USD, and your debt will not be passed on if they die. You can pull a lever to switch the trolley to a track where no one is tied.",
    "A trolley is headed towards a track where 1 person is tied. You owe them 600,000 USD, and your debt will not be passed on if they die. You can pull a lever to switch the trolley to a track where 1 person is tied.",
    "A trolley is headed towards a track where 40% of the global population has somehow been tied. You can pull a lever to switch the trolley to a track where no one is tied.",
    "A trolley is headed towards a track where a field-leading climate activist is tied. You can pull a lever to switch the trolley to a track where a field-leading social justice activist is tied.",
    "A trolley is headed towards a track where your favourite actor is tied. You can pull a lever to switch the trolley to a track where your favourite author is tied."
    "A trolley is headed towards a track where 5 people are tied. You can pull a lever to switch the trolley to a track where it will enter a time machine and kill 5 people 100 years in the future.",
    "A trolley is headed towards a track where 5 people are tied. You can pull a lever to switch the trolley to a track where it will enter a tunnel and emerge in a distant country where 5 people are tied.",
]


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
