### First steps
- When contributing to this repository, please open an issue first and explain the change- feature, bug, optimization?
    - describe the issue as clearly as possible
    - platform details
    - usage details
    - what did you expect to happen
    - what actually happened

### Pull requests

1. Please follow this [commit naming convention](https://www.conventionalcommits.org/en/v1.0.0/)
   and keep a level of verbosity(comments in the code etc.)
2. Update the README.md with details of changes, this includes any major changes that
   result to changes in the usage of the API.

### Getting started locally

## Requirements

- python 3
- requests lib
- [poetry](https://python-poetry.org/) for virtual development environment
- [pyinstaller](https://pyinstaller.readthedocs.io) for building and testing

## How to install

1. After installing poetry, install the dependencies with it.
2. For building, use the following command: ``` pyinstaller --onefile src/service_status_checker/main.py --name service-status-checker -p /your_path/service-status-checker/src/service_status_checker ```

That's it! Now you're ready to start contributing!
