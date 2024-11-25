#db_config에서 쿼리를 불러온다.
from db_config import conn, cursor

#print(cursor)

cursor.execute('''
               CREATE TABLE IF NOT EXISTS tbpost_board(
               idx INT AUTO_INCREMENT PRIMARY KEY,
               stock varchar(100),
               url varchar(10000),
               title varchar(100),
               -- mysql은 varchar(max)없다고 하네
               -- 대신, varchar(65536)
               investment varchar(100),
               post_date datetime,
               price varchar(100),
               position varchar(100)                     
               
               )
               ''')

conn.commit()

print('테이블 생성함')


