from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/insultar")
async def insultoEndPoint(insulto: str, elogio: str):
    return {"insulto": f"Eres un poco {insulto} pero tambien {elogio}"}


@app.get("/elogiar/{elogio}")
async def insultoEndPoint(elogio: str):
    return {"insulto": f"Eres un poco {elogio}"}
