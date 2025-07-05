# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "CropHealthNet++ backend working!"}
