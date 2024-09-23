
from requests import Response
def raise_if_its_not_ok(response:Response):
    if response.status_code <= 200 or response.status_code >= 300:
        raise Exception(response.json())
