from fastapi import FastAPI
from orm_from_llm import Base, lifespan

app = FastAPI(lifespan=lifespan)

def main():
    return {"message": "AI chatbot in telegramm"}