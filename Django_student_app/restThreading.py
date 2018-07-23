import threading
import requests
import json
import time


def make_request(id):
    url = "http://127.0.0.1:8000/api/v1/college/"+str(id)+"/students/"
    # print(url)
    response = requests.get(url)
    json_data = json.loads(response.text)
    print(json_data)


if __name__ == '__main__':
    thread=[]
    start=time.time()
    for i in range(1,10):
        thread.append( threading.Thread(target=make_request(i)))
        thread[i-1].start()

    for i in range(0,9):
        thread[i].join()

    print(time.time()-start)

    print("\nDone\n")
