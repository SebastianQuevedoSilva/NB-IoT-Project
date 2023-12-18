# NB-IoT-Project

A continuación ciertos puntos respecto a los archivos desplegados en este repositorio:

- app.py no fue utilizada realmente, en un principio la idea fue desarrollar todos los servicios para desplegarlos en una VM, luego por tiempo no se alcanzó a terminar. De la misma manera las carpetas templates y static hacen referencia al proyecto incompleto del Framework Flask, el cual manejaría el backend y frontend de la app.
- prueba.cpp corresponde al código cargado en el Hardware StarterKitNB, el cual fue testeado durante la presentación del día viernes 17-12-2023
- publisher.py corresponde al módulo de pruebas donde se subió información al broker de manera sintética para validar el correcto funcionamiento del servidor como del almacenaje de datos
- sensor_tables.sql son los comandos utilizados para crear el esquema de recepción de los datos
- subscriber.py es el encargado de recolectar los datos de manera local y hace el guardado de los datos en las tablas correspondientes.
- La carpeta databases contiene la lógica del código para almacenar los datos
