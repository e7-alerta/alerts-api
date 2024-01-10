from fastapi import FastAPI

from manager import alert_manager, hook_manager
from manager.phone_alert_handler import handle_phone_alert
from manager.hook_manager import handle_device_alert

from manager.alert_manager import handle_phone_button_alert, handle_tuya_device_alert

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello alerts 1.3"}


@app.post("/api/v1/hooks/phones/handler_alert")
async def handler_alert(body: dict):
    print("handler_alert of phone", body)
    handle_phone_alert(body)
    # alert_manager.process_alert()
    # hook_manager.handler_alert(body)

    return {"mensaje": "alerta notificada"}


@app.post("/api/v1/hooks/devices/handler_alert")
async def handler_alert(body: dict):
    print("handler_alert of device", body)
    # alert_manager.process_alert()
    handle_device_alert(body)

    return {"mensaje": "alerta notificada"}


@app.get("/api/v1/alarms/tuya-device/{tuya_id}")
async def tuya_alert(tuya_id: str, sos: bool = False):
    print(f"tuya_id: {tuya_id} and sos: {sos}")
    handle_tuya_device_alert(tuya_id, sos=sos)

    return {"mensaje": "alerta recibida", "tuya_id": tuya_id}


@app.get("/api/v1/fotton/{phonebtn_id}/entry")
async def phonebtn_alert(phonebtn_id: str, alarm_type: str = None):
    print(f"phonebtn_id: {phonebtn_id}")
    handle_phone_button_alert(phonebtn_id, alert_type=alarm_type)

    return {"mensaje": "alerta recibida", "phonebtn_id": phonebtn_id}


@app.get("/api/v1/fotton/{phonebtn_id}/trigger_alarm")
async def phonebtn_alert(phonebtn_id: str, alarm_type: str = "sos"):
    print(f"phonebtn_id: {phonebtn_id}  and alarm_type: {alarm_type}")
    handle_phone_button_alert(phonebtn_id)

    return {"mensaje": "alerta recibida", "phonebtn_id": phonebtn_id}


@app.get("/api/v1/alarms/phonebtn/{phonebtn_id}")
async def phonebtn_alert(phonebtn_id: str):
    print(f"phonebtn_id: {phonebtn_id}")
    handle_phone_button_alert(phonebtn_id)

    return {"mensaje": "alerta recibida", "phonebtn_id": phonebtn_id}


@app.get("/api/v1/alarms/phonebtn/{phonebtn_id}")
async def phonebtn_alert(phonebtn_id: str):
    print(f"phonebtn_id: {phonebtn_id}")
    handle_phone_button_alert(phonebtn_id)

    return {"mensaje": "alerta recibida", "phonebtn_id": phonebtn_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8060)
