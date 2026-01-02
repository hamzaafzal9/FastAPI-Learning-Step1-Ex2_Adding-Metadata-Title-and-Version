from fastapi import FastAPI

app = FastAPI(
    title = "My Inventory API",
    description = "This is a Basic API to learn FastAPI",
    version = "1.0.0"
)

@app.get("/info")
async def get_info():
    return {"app_name":"Inventory API", "Status":"Active"}

    

    