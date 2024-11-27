# 이진 검색

## 함수
import random

def binSearch(array, finddata):
    pos = -1
    start = 0
    end = len(array) - 1

    while (start <= end):
        middle = (start + end) // 2 #나머지 버림
        if (array[middle] == finddata):
            pos = middle
            break
        elif (array[middle] < findData):
            start = middle + 1
        else:
            end = middle - 1
    return pos




## 변수
dataArray = [random.randint(30,199) for _ in range(8)]
findData = random.choice(dataArray)
dataArray.sort()


## 메인
print('배열', dataArray)
position = binSearch(dataArray, findData)
if (position != -1):
    print(findData, '는', position, '위치에 있어요')

else :
    print(findData, '는 없어요 ㅜ')



