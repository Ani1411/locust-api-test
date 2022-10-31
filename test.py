from urllib.parse import urlparse
from threading import Thread
import http.client, sys
from queue import Queue

import requests

concurrent = 200
url = 'http://3.110.147.243:8089/engine/postcode?postcode=CT91SD&beds=2&baths=2'
urls = [url]*100

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()


def getStatus(ourl):
    try:
        r = requests.get(url)

        return r.status_code, r.elapsed.total_seconds()
    except:
        return "error", ourl


def doSomethingWithResult(status, url):
    print(status, url)


q = Queue(concurrent * 2)
for _ in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in urls:
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
