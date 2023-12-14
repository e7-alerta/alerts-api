import dash.api.stores_api as dash
from dash.types import Store


def update(store: Store) -> Store:
    return dash.update(store)
