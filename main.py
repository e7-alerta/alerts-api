from fastapi import FastAPI

from manager import alert_manager, hook_manager

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/v1/hooks/devices/handler_alert")
async def handler_alert(body: dict):
    print("handler_alert", body)
    # alert_manager.process_alert()
    hook_manager.handler_alert(body)

    return {"mensaje": "alerta notificada"}


@app.get("/api/v1/alarms/tuya-device/{tuya_id}")
async def tuya_alert(tuya_id: str, sos: bool = False):
    print(f"tuya_id: {tuya_id} and sos: {sos}")
    alert_manager.process_tuya_device_alert(tuya_id, sos=sos)

    return {"mensaje": "alerta recibida", "tuya_id": tuya_id}


@app.get("/api/v1/alarms/phonebtn/{phonebtn_id}")
async def phonebtn_alert(phonebtn_id: str):
    print(f"phonebtn_id: {phonebtn_id}")
    alert_manager.process_phone_button_alert(phonebtn_id)

    return {"mensaje": "alerta recibida", "phonebtn_id": phonebtn_id}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)