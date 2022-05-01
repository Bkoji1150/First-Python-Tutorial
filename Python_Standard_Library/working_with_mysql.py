import mysql.connector as mysql
from mysql.connector import Error
import json
from pathlib import Path
from pprint import pprint

try:
    with mysql.connect(host='localhost',
                        database='Electronics',
                        user='root',
                        auth_plugin='hsgdgd!2'
    ) as conn:
        if conn.is_connected():
            # db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            # cursor = conn.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
            # print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
