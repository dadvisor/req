import time

import requests

if __name__ == '__main__':
    running = True

    while running:
        try:
            r = requests.get('http://web:5000/')
            print(r.text)
            time.sleep(1)
        except KeyboardInterrupt:
            running = False
        except Exception as e:
            print(e)
