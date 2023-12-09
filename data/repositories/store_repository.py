import dash.api.stores_api as dash
from dash.types import Store


def update(store: Store) -> Store:
    """
    deletage a la api de dash
    :param store:
    :return:
    """
    return dash.update(store)
