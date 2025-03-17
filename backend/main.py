from fastapi import FastAPI
from app.routes import governance

# Initialize FastAPI app
app = FastAPI(title="AI Governance API", version="1.0")

# Include API routes
app.include_router(governance.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Open-Source AI Governance Tool API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
