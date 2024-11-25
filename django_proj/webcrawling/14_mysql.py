import csv
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
print(config)
conn = pymysql.connect(**config)

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Rank_index INT,
                    title VARCHAR(255),
                    author VARCHAR(255),
                    -- genre VARCHAR(255),
                    price DECIMAL(10,2)
               )
''')

with open('book_list.csv', mode = 'r', encoding = 'utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        
        Rank_index, title, author, price = i
        # print(Rank_index)
        # print(title)
        # print(author)
        # print(price)
        # print("***")
        # print(f'i :{i}')

        # print("***")
        price = float(price.replace('원','').replace(',',''))
        cursor.execute('''
                       INSERT INTO books ( Rank_index, title , author, price )
                       values( %s, %s,%s,%s )
                       ''', (Rank_index, title, author, price)

                       )
        

conn.commit()
cursor.close()
conn.close()