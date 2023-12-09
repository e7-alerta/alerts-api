from enum import Enum

import requests

from dash.types import Store, store_load


def update(
    store: Store
) -> Store:
    url = f"https://dash.vecinos.com.ar/items/places/{store.id}"

    payload = {
        "alerted": store.alerted,
        "alert_type": store.alert_type.value,
        "status": store.status.value
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, json=payload)
    print(response.text)
    data = response.json()["data"]
    store = store_load(data)
    return store