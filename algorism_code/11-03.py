## 함수
import random
def selectSort(array):
    n = len(array) # 데이터 개수
    for i in range(0, n-1): #사이클 (큰 회전)
        minIdx = i
        for j in range(i + 1, n): #작은 반복문
            if (array[minIdx] > array[j]):
                minIdx = j
        array[i], array[minIdx] = array[minIdx], array[i] # 데이터 교환
    return array

## 변수
dataArray = [random.randint(30,190) for _ in range(4)]

## 메인
print(dataArray)
dataArray = selectSort(dataArray)


print(dataArray)