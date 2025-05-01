from fastapi import FastAPI
import uvicorn
from auth.routes import router as auth_router
from users.routes import router as user_router
from chat.routes import router as chat_router
from mangum import Mangum

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags = ["Authentication"])
app.include_router(user_router, prefix="/user", tags = ["user"])
app.include_router(chat_router, prefix="/chat", tags = ["chat"])

handler = Mangum(app)

@app.get("/")
def read_root():
    return {"message": "welcome to my fastapi project"}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)