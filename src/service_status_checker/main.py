import request


if __name__ == '__main__':
    service = input("Network service: ")
    service = str(service)

    print(request.is_service_online(service))

