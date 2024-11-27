## 함수
def openBox():
    global count
    print(f'박스 {count}번 열었습니다~')
    count -= 1
    if count == 0:
        print('** 선물 발견 **')
        return
    else:
        openBox()
        

    return



## 메인
count = 10

openBox()