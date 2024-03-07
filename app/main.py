from dotenv import load_dotenv
from fastapi import FastAPI
from routes import router
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
# app.mount("/app/user", StaticFiles(directory="app/user"), name="app/user")


def main():
    """
    Entry point of the application.
    """
    app.run()

if __name__ == "__main__":
    main()