from threading import Thread


class LoadThread(Thread):

    def __init__(self, iterations):
        Thread.__init__(self)
        self.iterations = iterations
        self.result = -1

    def run(self):
        s = 0
        for i in range(self.iterations):
            s += i
        self.result = s
