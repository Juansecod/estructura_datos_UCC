from pandas import DataFrame
import requests
from Lista import Lista

def llenar_lista(urls, lista):
    for url in urls:
        features = []
        data = requests.get(url)
        for feature in data.json()["features"]:
            features.append(feature["properties"])
        df = DataFrame(features)
        lista.insertar(df)
        

historico = Lista()
urls = [
    "https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/16/query?outFields=*&where=1%3D1&f=geojson",
    "https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/17/query?outFields=*&where=1%3D1&f=geojson",
    "https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/18/query?outFields=*&where=1%3D1&f=geojson",
    "https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/19/query?outFields=*&where=1%3D1&f=geojson",
    "https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_accidentes_2022_gdb/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
]   
llenar_lista(urls,historico)

historico.mostrar()