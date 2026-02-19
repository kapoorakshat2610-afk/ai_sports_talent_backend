from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend running"}

@app.get("/test")
def test():
    return {"test": "success"}
