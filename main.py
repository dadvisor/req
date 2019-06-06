import os
import time

import requests

from LoadThread import LoadThread

if __name__ == '__main__':
    running = True

    addresses = os.environ.get('HOST', 'web:5000').split(',')
    print('Addresses: {}'.format(addresses))
    iterations = int(os.environ.get('ITERATIONS', 10 ** 8))
    print('Iterations: {}'.format(iterations))

    sleep_time = int(os.environ.get('SLEEP_TIME', 5))
    print('Sleep time: {}'.format(sleep_time))

    while running:
        try:
            for a in addresses:
                r = requests.get('http://{}/'.format(a))
            time.sleep(sleep_time)
            if iterations > 0:
                LoadThread(iterations).start()
        except KeyboardInterrupt:
            running = False
        except Exception as e:
            print(e)
