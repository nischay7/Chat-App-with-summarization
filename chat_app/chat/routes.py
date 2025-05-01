import os
from fastapi import APIRouter, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.websockets import WebSocket, WebSocketDisconnect
from .connection_manager import ConnectionManager

router = APIRouter()
templates = Jinja2Templates(directory="chat/templates")
manager = ConnectionManager()


@router.get("/home")
def root(request: Request):
    return templates.TemplateResponse(
        request,
        'chat_home.html',
        {"ws_endpoint": f"ws://{request.headers.get("host")}/chat/ws"}
    )

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"client {websocket.client.host}:{websocket.client.port} says {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast("Client disconnected")

