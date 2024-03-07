import uvicorn
from fastapi import FastAPI, Depends
import os
from pydantic import BaseModel
from auth import get_current_token

app = FastAPI()


@app.get("/")
async def root(token: str = Depends(get_current_token)):
    return {"message": "Hello, world!"}

port = int(os.getenv('PORT', '8000'))
uvicorn.run(app, host="0.0.0.0", port=port)