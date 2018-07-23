import threading
import time
import logging
import random
import queue
import requests
import json


BUF_SIZE = 4
q = queue.Queue(BUF_SIZE)
lock= threading.Lock()
list_queue = []



class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if len(list_queue)<4:
                item = random.randint(1, 10)
                lock.acquire()
                list_queue.append(item)

                # q.put(item)
                time.sleep(random.random())
                lock.release()
        return



class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if list_queue != []:
                # item = q.get()
                item=list_queue.pop()

                url = "http://127.0.0.1:8000/api/v1/college/" + str(item) + "/students/"
                # print(url)
                response = requests.get(url)
                json_data = json.loads(response.text)
                print(json_data)
                time.sleep(random.random())
        return


if __name__ == '__main__':

    c = ConsumerThread()
    p = ProducerThread()

    p.start()
    c.start()
    p.join()
    c.join()
    time.sleep(2)
    time.sleep(2)