import sys
import request


if __name__ == '__main__':
    try:
        request.main_loop()
    except KeyboardInterrupt as e:
        print('\nExiting by user request. Goodbye\n')
        sys.exit(0)

