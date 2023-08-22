from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"From: {os.environ.get('HOSTNAME', 'DEFAULT_ENV')}"}