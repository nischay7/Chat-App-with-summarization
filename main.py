from fastapi import FastAPI
from auth.routes import router as auth_router
from users.routes import router as user_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags = ["Authentication"])
app.include_router(user_router, prefix="/user", tags = ["user"])

@app.get("/")
def read_root():
    return {"message": "welcome to my fastapi project"}