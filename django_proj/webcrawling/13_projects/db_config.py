import pymysql

# 이거 쓰려면 pip istall python-dotenv
from dotenv import load_dotenv
import os

#환경변수 읽기
load_dotenv()


config ={
    'user'    : os.getenv('user'),
    'password' : os.getenv('password'),
    'host' : 'localhost',
    'database' : 'my_db'
}

conn = pymysql.connect(**config)

cursor = conn.cursor()
