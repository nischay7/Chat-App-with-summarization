import os
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

router = APIRouter()
templates = Jinja2Templates(directory="chat/templates")

class ConnectionManager:
    AWS_WEBSOCKET_http_URL= os.environ.get("AWS_WEBSOCKET_http_URL")
    AWS_WEBSOCKET_ep_URL= os.environ.get("AWS_WEBSOCKET_http_URL")

@router.get("/home")
def root(request: Request):
    return templates.TemplateResponse(
        request,
        'chat_home.html',
        {"ws_endpoint": f"{ConnectionManager.AWS_WEBSOCKET_ep_URL}"}
    )
