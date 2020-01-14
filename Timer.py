
import threading


class RepeatingTimer(threading.Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


if __name__ == '__main__':
    from datetime import datetime
    import time
    ts = []
    for i in range(2):
        t = RepeatingTimer(3, lambda: print('{}'.format(datetime.now())))
        ts.append(t)
        t.start()

    print('wait...')
    time.sleep(10)

    for t in ts:
        t.cancel()
    print('end')
