from dash.mapper import phone_load
from data.repositories import store_repository
from dash.types import StoreAlertType, store_load


def handle_phone_alert(payload: dict):
    print("handler_alert", payload)

    phone = phone_load(payload["phone"])
    store = store_load(payload["store"])
    changes = payload["changes"]
    type = payload["type"]

    if phone.alerted:
        # check if store is alerted
        if store.alerted:
            print(f"store {store.id} is already alerted")
            return {"mensaje": "store is already alerted"}
        else:
            # update store to alerted
            store.alerted = True

            # el tipo de alerta depende del tipo de dispositivo alertado
            if StoreAlertType.SAQUEO_ALERT == phone.alert_type:
                store.alert_type = StoreAlertType.SAQUEO_ALERT
            elif StoreAlertType.INCENDIO_ALERT == phone.alert_type:
                store.alert_type = StoreAlertType.INCENDIO_ALERT
            elif StoreAlertType.ACCIDENTE_ALERT == phone.alert_type:
                store.alert_type = StoreAlertType.ACCIDENTE_ALERT
            elif StoreAlertType.ACTIVIDAD_SOSPECHOSA_ALERT == phone.alert_type:
                store.alert_type = StoreAlertType.ACTIVIDAD_SOSPECHOSA_ALERT
            else:
                store.alert_type = StoreAlertType.SAQUEO_ALERT

            store = store_repository.update(store)
            print(f"store {store.id} is alerted")

            return {"mensaje": "store is alerted"}

    return {"menses": "alerta notificada"}
