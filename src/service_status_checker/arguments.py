import argparse


def initialize_arguments():
    parser = argparse.ArgumentParser(description='Checks HTTP services for availability every n amount of time.')
    parser.add_argument('--disable-ssl',
                        action='store_true',
                        help='Disables SSL verification. Can be used for services with self signed certificates '
                             'or local services. This will still not suppress the warning.')
    parser.add_argument('--interval',
                        action='store',
                        required=True,
                        help='The scheduled time interval of the requests in seconds.')
    parser.add_argument('--services',
                        action='store',
                        nargs="*",
                        required=True,
                        help='The services IP addresses or the domain names. Can take one or more space separated arguments. '
                             'The format can be 127.0.0.1:8080 or https://127.0.0.1:8080 and '
                             'foo.com or https://foo.com.'
                             'The protocol can be omitted, in which case the default "http" will be added automatically.')
    arguments = parser.parse_args()

    return arguments

