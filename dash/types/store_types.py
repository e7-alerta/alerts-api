from enum import Enum
from typing import Optional
from pydantic import BaseModel, UUID4

"""

[
    {
        "text": "Online",
        "value": "online"
    },
    {
        "text": "Alertado",
        "value": "alerted"
    },
    {
        "text": "Offline",
        "value": "draft"
    },
    {
        "text": "$t:published",
        "value": "published"
    },
    {
        "text": "$t:archived",
        "value": "archived"
    }
]

"""


class StoreStatus(Enum):
    ONLINE = "online"
    ALERTED = "alerted"
    OFFLINE = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class StoreAlertType(Enum):
    MINI_ALARM_ALERT = "mini_alarm_alert"
    ALARM_BUTTON_ALERT = "alarm_button_alert"
    MOTION_SENSOR_ALERT = "motion_sensor_alert"
    DOOR_CONTACT_ALERT = "door_contact_alert"
    DEVICE_ALERT = "device_alert"
    SILENT_ALERT = "silent_alert"
    APP_ALERT = "app_alert"
    MAP_BUTTON_ALERT = "map_button_alert"
    PHONE_BUTTON_ALERT = "phone_button_alert"
    SAQUEO_ALERT = "saqueo_en_comercio"
    ACTIVIDAD_SOSPECHOSA_ALERT = "actividad_sospechosa"
    ACCIDENTE_ALERT = "accident"
    INCENDIO_ALERT = "incendio_en_comercio"


"""
  "store": {
    "id": "957c990f-7818-465d-90b9-2d48e93d336b",
    "status": "online",
    "date_created": "2023-12-03T08:15:03.914Z",
    "date_updated": "2023-12-03T08:15:05.546Z",
    "geopoint": {
      "type": "Point",
      "coordinates": [
        -58.4242938,
        -34.6723701
      ]
    },
    "name": "",
    "address": "Coronel D Elia 3895, Provincia de Buenos Aires",
    "street": "Coronel D Elia",
    "street_number": 3895,
    "postal_code": "B1822",
    "place_type": null,
    "neighborhood": null,
    "photo": null,
    "raw_region": "Lanús",
    "raw_subregion": "Valentín Alsina",
    "raw_neighborhood": null,
    "raw_city": null,
    "raw_country": null,
    "raw_district": "Provincia de Buenos Aires",
    "alerted": false,
    "country_code": "AR",
    "contacto": null,
    "phone": null,
    "token": "ExponentPushToken[E_vl9xAvlgTEWaTMOx1HJU]",
    "alert_type": null,
    "subregion": null,
    "gplaces": [],
    "iot_devices": [
      "5095c22c-e272-4834-b124-20f45b55e4cc"
    ],
    "contacts": []
  },
"""


class Store(BaseModel):
    id: str
    name: Optional[str] = None
    place_type: Optional[str] = None
    status: StoreStatus = None
    alerted: Optional[bool] = False
    alert_type: Optional[StoreAlertType] = None
    geo_point: Optional[dict] = None
    street: Optional[str] = None
    street_number: Optional[int] = None
    neighborhood: Optional[str] = None
    subregion: Optional[str] = None
    contacto: Optional[str] = None
    phone: Optional[str] = None
    contacts: Optional[list] = []
    iot_devices: Optional[list] = []
    token: Optional[str] = None


def store_load(item):
    """
    Map a store from a dict.
    ignore empty fields
    :param item:
    :return:
    """
    print(item)
    store = Store(
        id=item["id"],
        name=item["name"],
        place_type=item["place_type"],
        status=item["status"],
        alerted=item["alerted"],
        alert_type=item["alert_type"],
        geo_point=item["geopoint"],
        street=item["street"],
        street_number=item["street_number"],
        neighborhood=item["neighborhood"],
        subregion=item["subregion"],
        contacto=item["contacto"],
        phone=item["phone"],
        contacts=item["contacts"],
        iot_devices=item["iot_devices"],
        token=item["token"]
    )
    return store
