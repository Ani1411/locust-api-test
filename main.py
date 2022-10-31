import time
import requests
import datetime
import concurrent.futures

MAX_THREADS = 100
CONCURRENT_THREADS = 100

url = 'http://3.110.147.243:8089/engine/postcode?postcode=CT91SD&beds=2&baths=2'

response = requests.get(url)

# print(response.json())
print(response.elapsed.total_seconds())


def send_api_request():
    print('Sending API request: ', url)
    r = requests.get(url)
    print('Received: ', r.status_code, r.elapsed.total_seconds())


start_time = datetime.datetime.now()
print('Starting:', start_time)

with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
    futures = [executor.submit(send_api_request) for _ in range(CONCURRENT_THREADS)]

time.sleep(5)
end_time = datetime.datetime.now()
print('Finished. Start time:', start_time, 'duration: ', end_time - start_time)
