from dash.types import Device, DeviceStatus, DeviceType
from dash.types.phone_types import Phone, PhoneStatus

"""
 { 'id': 'b6a595c9-257e-43a5-b157-3b532d41f47f', 
    'status': 'online', 
    'date_created': '2023-12-14T19:01:15.029Z', 
    'date_updated': '2023-12-14T22:22:55.475Z', 
    'phone_number': '1136206603', 
    'geopoint': {'type': 'Point', 'coordinates': [-58.401959, -34.6184936]}, 
    'name': 'Gabriel Simionato', 
    'contact': '168c5959-ef52-417c-8740-17db8f59d6ab', 
    'place': '25a8a44c-8537-439a-892d-df2f51528b98', 
    'push_token': 'ExponentPushToken[dX0rL3AiD9q90-JC7jIScI]', 
    'alerted': True, 
    'alert_type': 'saqueo_en_comercio', 
    'alert_point': None, 'devices': []
}
"""


def phone_load(item):
    print(item)
    return Phone(
        id=item["id"],
        status=PhoneStatus(item["status"]),
        alerted=item["alerted"],
        alert_type=item["alert_type"],
        alert_point=item["alert_point"],
        phone_number=item["phone_number"],
        push_token=item["push_token"],
        name=item["name"],
        contact=item["contact"],
    )


def device_load(item):
    print(item)
    return Device(
        id=item["id"],
        status=DeviceStatus(item["status"]),
        alerted=item["alerted"],
        sos=item["sos"],
        device_type=DeviceType(item["device_type"]),
        device_id=item["device_id"],
        name=item["device_name"],
        tuya_device=item["tuya_device"],
        tuya_id=item["tuya_id"],
        place_id=item["place"]
    )
