import uvicorn
from fastapi import FastAPI
from routes import monitor, vm_routes

app = FastAPI()

app.include_router(monitor.router, prefix="/api", tags=["Monitoramento"])
app.include_router(vm_routes.router, prefix="/api", tags=["VMs"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
