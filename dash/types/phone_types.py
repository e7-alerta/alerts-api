from enum import Enum
from typing import Optional

from pydantic import BaseModel, UUID4


class PhoneStatus(Enum):
    ALERTED = "alerted"
    ONLINE = "online"
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class PhoneAlertType(Enum):
    SAQUEO_ALERT = "saqueo_en_comercio"
    ACTIVIDAD_SOSPECHOSA_ALERT = "actividad_sospechosa"
    ACCIDENTE_ALERT = "accident"
    INCENDIO_ALERT = "incendio_en_comercio"


"""
    Phone data json example:
	"data": {
		"id": "b6a595c9-257e-43a5-b157-3b532d41f47f",
		"status": "online",
		"date_created": "2023-12-14T19:01:15.029Z",
		"date_updated": "2023-12-14T19:04:50.367Z",
		"phone_number": "1136206603",
		"geopoint": {
			"type": "Point",
			"coordinates": [
				-58.401959,
				-34.6184936
			]
		},
		"name": "Gabriel Simionato",
		"contact": "168c5959-ef52-417c-8740-17db8f59d6ab",
		"place": "25a8a44c-8537-439a-892d-df2f51528b98",
		"push_token": "ExponentPushToken[dX0rL3AiD9q90-JC7jIScI]",
		"alerted": false,
		"alert_type": null,
		"alert_point": null,
		"devices": []
	}

"""


class Phone(BaseModel):
    id: str
    status: PhoneStatus
    alerted: bool = False
    alert_type: Optional[PhoneAlertType] = None
    alert_point: Optional[dict] = None
    phone_number: Optional[str] = None
    push_token: Optional[str] = None
    name: Optional[str] = None
    contact: Optional[str] = None
    place: Optional[str] = None
    devices: Optional[list] = []
    geo_point: Optional[dict] = None
    place_id: Optional[str] = None
