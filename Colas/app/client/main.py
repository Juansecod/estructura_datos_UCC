import pandas as pd
import requests
import threading

def consulta(url):
    r = requests.get(url)
    print(r.json())

hilos = []
for url in ["http://localhost:8000/productos", "http://localhost:8000/carts", "http://localhost:8000/users", ]:
    hilo = threading.Thread(target=consulta, args=[url])
    hilos.append(hilo)

for f in hilos:
    f.start()
