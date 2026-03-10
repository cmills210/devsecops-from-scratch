from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevSecOps From Scratch API"}

@app.get("/health")
def health():
    return {"status": "ok"}

def add(a, b):
    return a + b
