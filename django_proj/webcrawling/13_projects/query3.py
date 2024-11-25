from db_config import conn, cursor

DBMS_DB = cursor.execute('''
               select * from tbpost_board;
               ''')

print(f'해당 테이블에 {DBMS_DB}개 있습니다')
conn.commit
cursor.close()
conn.close()