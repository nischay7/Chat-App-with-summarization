from fastapi.websockets import WebSocket
from fastapi import HTTPException

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_to_someone(self, message: str, websocket: WebSocket):
        if websocket in  self.active_connections:
            await websocket.send_text(message)
            return
        raise HTTPException(status_code=404, detail="User not online")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
