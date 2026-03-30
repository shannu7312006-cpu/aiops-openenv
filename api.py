from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.post("/step")
def step(action: dict):
    return {
        "observation": {"msg": "step done"},
        "reward": 1.0,
        "done": False,
        "info": {}
    }

@app.get("/state")
def state():
    return {"state": "running"}