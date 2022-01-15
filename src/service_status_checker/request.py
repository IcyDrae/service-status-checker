import requests


def make_head_request(ip):
    request = requests.request("head", ip)

    return request

