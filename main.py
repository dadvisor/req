import os
import time

import requests

if __name__ == '__main__':
    running = True

    addresses = os.environ.get('HOST', 'web:5000').split(',')
    print('Addresses: {}'.format(addresses))

    while running:
        try:
            for a in addresses:
                r = requests.get('http://{}/'.format(a))
                print(r.text)
            time.sleep(5)
        except KeyboardInterrupt:
            running = False
        except Exception as e:
            print(e)
