![GitHub](https://img.shields.io/github/license/MatrixEternal/service-status-checker?style=flat-square)
![GitHub](https://img.shields.io/github/v/release/MatrixEternal/service-status-checker?style=flat-square)
![GitHub](https://img.shields.io/github/last-commit/MatrixEternal/service-status-checker/main?style=flat-square)

# service-status-checker

This monitoring tool checks multiple HTTP services for availability on a scheduled basis. It uses the HEAD verb instead
of pinging the network, ensuring more reliable results. Its support for multiple services makes it a good use in a micro-service oriented architecture.
The conditions for a service to be considered available are:
1. Response code should be 200
2. There should not be a redirect to another service, defeating the purpose.


## In action

<img alt="Both services working" src="https://github.com/MatrixEternal/service-status-checker/blob/main/assets/both_services_available.gif" width="600">
<br>
<img alt="One service down" src="https://github.com/MatrixEternal/service-status-checker/blob/main/assets/one_service_down.gif" width="600">


## Arguments

```
usage: service-status-checker [-h] [--disable-ssl] --interval INTERVAL --services [SERVICES [SERVICES ...]]

Checks HTTP services for availability every n amount of time.

optional arguments:
  -h, --help            show this help message and exit
  --disable-ssl         Disables SSL verification. Can be used for services with self signed certificates or local
                        services. This will still not suppress the warning.
  --interval INTERVAL   The scheduled time interval of the requests in seconds.
  --services [SERVICES [SERVICES ...]]
                        The services IP addresses or the domain names. Can take one or more space separated
                        arguments. The format can be 127.0.0.1:8080 or https://127.0.0.1:8080 and foo.com or
                        https://foo.com.The protocol can be omitted, in which case the default "http" will be
                        added automatically.
```

## How it is built

This software is built using [pyinstaller](https://pyinstaller.readthedocs.io) and it is only built for Linux, the target being a binary executable.

## Download
[Releases](https://github.com/MatrixEternal/service-status-checker/releases)

## Contributing
Please head to [the contributors documentation](CONTRIBUTORS.md).

## License
[GPLv3](LICENSE.txt)
