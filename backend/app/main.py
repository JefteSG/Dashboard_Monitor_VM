import uvicorn
from fastapi import FastAPI
from routes import vm_routes
from routes.monitor import monitor_vms_ws

app = FastAPI()

app.include_router(vm_routes.router, prefix="/api", tags=["VMs"])
app.add_api_websocket_route("/ws/monitor", monitor_vms_ws)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
