from fastapi import FastAPI
from api.routers.vms import router as vms_router

app = FastAPI()
app.include_router(vms_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
