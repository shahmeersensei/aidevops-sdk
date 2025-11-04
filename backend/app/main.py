from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def root():
    """Root endpoint — helpful for browsers or tooling that hit '/'.

    Returns the same payload as /health so clients don't get a 404 at '/'.
    """
    return JSONResponse({"status": "ok", "message": "AI DevOps Backend running smoothly", "endpoint": "/health"})


@app.get("/health")
def health():
    return {"status": "ok", "message": "AI DevOps Backend running smoothly"}
