import requests
import arguments


request_method = "head"
default_protocol = "http"
args = arguments.initialize_arguments()


def is_service_online(service: str):
    address = handle_address(service)
    print(args)

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
    ssl = True
    if args.disable_ssl:
        ssl = False

    request = requests.request(
        request_method,
        address,
        timeout=5,
        verify=ssl
    )

    return request

