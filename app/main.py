from dotenv import load_dotenv
from fastapi import FastAPI
from routes import router
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import os

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("session_secret_key"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

def main():
    """
    Entry point of the application.
    """
    app.run()

if __name__ == "__main__":
    main()