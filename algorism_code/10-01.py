## 함수
count = 0
def openBox():    
    global count
    while count <= 3:
        print('상자를 엽니다')
        count += 1
        openBox()
        

## 메인
openBox()