
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Add this CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crophealthnet-frontend.vercel.app"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "CropHealthNet++ backend is live!"}
