import argparse


def initialize_arguments():
    parser = argparse.ArgumentParser(description='Checks an HTTP service for availability.')
    parser.add_argument('--disable-ssl',
                        action='store_true',
                        help='Disables SSL verification. Can be used for services with self signed certificates '
                             'or local services. This will still not suppress the warning.')
    arguments = parser.parse_args()

    return arguments
