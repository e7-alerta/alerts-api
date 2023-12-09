from manager import device_manager


def process_tuya_device_alert(tuya_id, sos: bool = False):
    print(f"[tuya_device_alert] tuya_id: {tuya_id} and sos: {sos}")

    device = device_manager.find_by_tuya_id(tuya_id)

    if device.alerted:
        print(f"[tuya_device_alert] device {tuya_id} is already alerted")
        return

    device_manager.alert_device(device, sos=sos)
    pass


def process_phone_button_alert(phonebtn_id):
    """
    Chequea si el id del boton de panico existe en la base de datos
    si no existe, lo crea  y lo alerta
    si existe, chequea si esta alertado
    si esta alertado, no hace nada
    si no esta alertado, lo alerta
    :param phonebtn_id:
    :return:
    """
    print(f"[phone_button_manager] phonebtn_id: {phonebtn_id}")

    device = device_manager.find_or_create_device_by_id(phonebtn_id)

    if device.alerted:
        print(f"[phone_button_manager] device {phonebtn_id} is already alerted")
        return

    device_manager.alert_device(device, sos=True)
    pass
