import pymysql
import json
from datetime import datetime

DB_NAME = "nb_iot_monitoring_EL5207"
DB_USERNAME = "mqtt_client_2"
DB_PASSWORD = "mqtt_client_2"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

tables = {"temperatura":"TemperatureData","batery":"BatteryData","ppm":"PPMData"
,"humedad":"HumidityData"} 

with open("database/querys.json","r") as querys:
    QUERY_DICT = json.load(querys)

def getConnection():
    conn = pymysql.connect(
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    return conn

def get_data_from_table(table):
    c = getConnection()
    cursor = c.cursor()
    cursor.execute(QUERY_DICT[f'get_{table}'])
    data = cursor.fetchall()
    if data:
        return data #salida[:size]
    return None


def set_value(table, value):
    try:
        c = getConnection()
        cursor = c.cursor()
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        sql = f"INSERT INTO {tables[table]} (value,timestamp) VALUES ('{float(value)}','{timestamp}')"
        cursor.execute(sql)
        c.commit()
        print("registro exitoso")
        c.close()
    except Exception as e:
        print(f"Error al insertar en {table}: {str(e)}")
        c.rollback()