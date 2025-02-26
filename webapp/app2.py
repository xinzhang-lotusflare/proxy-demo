from fastapi import FastAPI

print("webapp-2 started")
app = FastAPI()

###
# Routers
###
@app.get("/")
async def root():
    return { "up": "webapp-2" }

@app.get("/broken", status_code=403)
async def broken():
    return {"error": "Not Good"}
