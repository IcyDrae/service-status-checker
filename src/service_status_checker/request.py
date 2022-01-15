import requests


request_method = "head"
default_protocol = "http"


def is_service_online(service: str):
    address = handle_address(service)

    try:
        request = make_request(address)
    except Exception as e:
        return e

    return request.status_code == 200 and not request.is_redirect


def handle_address(definition: str) -> str:
    delimiter = "://"

    if delimiter not in definition:
        address = default_protocol + delimiter + definition
    else:
        address = definition

    print(address)
    return address



def make_request(address):
    request = requests.request(
        request_method,
        address,
        timeout=5,
        verify=False
    )

    return request

