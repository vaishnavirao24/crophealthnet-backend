from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

app = FastAPI()

# ✅ CORS for Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crophealthnet-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CropHealthNet++ backend working!"}

# ✅ ADD THIS
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # 🧪 Dummy prediction for now
    prediction = "Apple Scab"

    return {"result": prediction}



import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render will set PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
