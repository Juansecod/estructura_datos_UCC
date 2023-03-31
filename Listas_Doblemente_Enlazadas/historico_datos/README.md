# Sistema historico de datos

Realizar una recoleccion de datos desde 2018 hasta la fecha que este disponible. La fuente de datos sera extraida de [Datos abiertos de medellin](https://geomedellin-m-medellin.opendata.arcgis.com). Los resultados que brinde la API seran guardadas en un DataFrame, el cual debera estar en una lista enlazada.

- [Incidentes georreferenciados 2018](https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/16/query?outFields=*&where=1%3D1&f=geojson)
- [Incidentes georreferenciados 2019](https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/17/query?outFields=*&where=1%3D1&f=geojson)
- [Incidentes georreferenciados 2020](https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/18/query?outFields=*&where=1%3D1&f=geojson)
- [Incidentes georreferenciados 2021](https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/19/query?outFields=*&where=1%3D1&f=geojson)
- [Incidentes georreferenciados 2022](https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_accidentes_2022_gdb/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson)

## Ejecución

Primero, necesitaremos instalar los requerimientos de la apliacion, para ello ejecutamos el siguiente comando:

```sh
pip install -r requirements.txt
```

Una vez con los requerimientos instalados, podemos ejecutar nuestra aplicacion con el siguiente comando:

```sh
python main.py
```
