
from dash.mapper import device_load
from dash.types import StoreAlertType, DeviceType, store_load
from data.repositories import store_repository


def handler_alert(payload: dict):
    """
    check si el device esta alertado
    se actualiza el store a alertado
    :param payload:
    :return:
    """
    print("handler_alert", payload)

    device = device_load(payload["device"])
    store =  store_load(payload["store"])
    changes = payload["changes"]
    type = payload["type"]

    if device.alerted:
        # check if store is alerted
        if store.alerted:
            print(f"store {store.id} is already alerted")
            return {"mensaje": "store is already alerted"}
        else:
            # update store to alerted
            store.alerted = True

            # el tipo de alerta depende del tipo de dispositivo alertado
            if DeviceType.MINI_ALARM == device.device_type:
                store.alert_type = StoreAlertType.MINI_ALARM_ALERT
            if DeviceType.PHONE_BUTTON == device.device_type:
                store.alert_type = StoreAlertType.PHONE_BUTTON_ALERT
            elif DeviceType.DOOR_CONTACT == device.device_type:
                store.alert_type = StoreAlertType.DOOR_CONTACT_ALERT
            elif DeviceType.MOTION_SENSOR == device.device_type:
                store.alert_type = StoreAlertType.MOTION_SENSOR_ALERT
            elif DeviceType.PHONE_BUTTON == device.device_type:
                store.alert_type = StoreAlertType.PHONE_BUTTON_ALERT
            elif DeviceType.ALARM_BUTTON == device.device_type:
                store.alert_type = StoreAlertType.ALARM_BUTTON_ALERT

            store = store_repository.update(store)
            print(f"store {store.id} is alerted")

            return {"mensaje": "store is alerted"}

    return {"menses": "alerta notificada"}