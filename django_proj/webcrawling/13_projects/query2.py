import csv
from db_config import conn, cursor

with open('13_project_stock.csv', mode = 'r', encoding = 'cp949') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        # print(i)
        stock = i[0]
        url = i[1]
        title = i[2]
        investment = i[3]
        post_date = i[4]
        price = i[5]
        position = i[6]
        
        # print(stock)
        # print(url)
        # print(title)
        # print(investment)
        # print(post_date)
        # print(price)
        # print(position)
        
        cursor.execute('''
                        INSERT  INTO tbpost_board
                        values(NULL, %s, %s, %s, %s, %s, %s, %s)
                       ''', (stock, url, title, investment, post_date, price, position)
                       )                       

conn.commit()
print('INSERT 완료')

