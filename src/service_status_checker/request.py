import time
import requests
import arguments


request_method = "head"
default_protocol = "http"
args = arguments.initialize_arguments()
interval = float(args.interval)

def main_loop():
    start_time = time.time()
    while True:
        time.sleep(
            interval - ((time.time() - start_time) % interval)
        )
        print("tick")

        print(is_service_online(str(args.service)))


def is_service_online(service: str):
    address = handle_address(service)

    try:
        request = make_request(address)
    except Exception as e:
        return e

    return request.status_code == 200 and \
           not request.is_redirect


def handle_address(definition: str) -> str:
    delimiter = "://"

    if delimiter not in definition:
        address = default_protocol + delimiter + definition
    else:
        address = definition

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

