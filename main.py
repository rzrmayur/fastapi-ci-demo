from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CI/CD pipeline is working with an update! AWESOME, recheck, l1"}

