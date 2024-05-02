import panel as pn
from bokeh.embed import server_document
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from tools.sta_ind.sta_ind_wid import app_instance
from tools.test2.pn_app import createApp2

app = FastAPI()
templates = Jinja2Templates(directory="/faststorage/project/genint2_develop/GenerationInterval_V2/src/templates")

@app.get("/staind")
async def bkapp_page(request: Request):
    script = server_document('http://127.0.0.1:2281/staind')
    return templates.TemplateResponse("base.html", {"request": request, "script": script})

@app.get("/app2")
async def bkapp_page2(request: Request):
    script = server_document('http://127.0.0.1:2281/app2')
    return templates.TemplateResponse("base.html", {"request": request, "script": script})

pn.serve({'/staind': app_instance, '/app2': createApp2},
        port=2281, allow_websocket_origin=["127.0.0.1:2281"],
        address="0.0.0.0", show=False)