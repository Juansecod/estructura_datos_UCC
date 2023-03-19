from pandas import DataFrame
import requests
import threading
from Queue import Queue

urls = Queue()
responses = Queue()

def fetch(condition, url):
    with condition:
        try:
            r = requests.get(url)
            df = DataFrame(r.json())
            responses.append(df)
        except:
            responses.append({"msg": "Bad Request"})
        condition.notify()


threads = []
condition = threading.Condition()
URL_BASE = "http://localhost:8000/"

for path in ["products", "carts", "users"]:
    url = URL_BASE + path
    urls.append(url)
    thread = threading.Thread(target=fetch, args=[condition, url])
    threads.append(thread)

for f in threads:
    f.start()

print("waiting...", end="\n")

with condition:
    condition.wait_for(lambda : responses.size() == urls.size())
    print("-"*100)
    print("Urls".center(100))
    print("-"*100, end="\n\n")
    urls.display()
    print("-"*100)
    print("Responses".center(100))
    print("-"*100)
    responses.display()
