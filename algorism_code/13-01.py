# 순차 검색

## 함수
import random

def seqSearch(array, finddata):
    pos = -1
    for i in range(len(array)):
        if (array[i] == finddata):
            pos = i
            break



    return pos




## 변수
dataArray = [random.randint(30,199) for _ in range(8)]
findData = random.choice(dataArray)
position = seqSearch(dataArray, findData)


## 메인
print('배열', dataArray)

if (position != -1):
    print(findData, '는', position, '위치에 있어요')

else :
    print(findData, '는 없어요 ㅜ')



