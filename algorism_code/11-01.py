## 함수
def findMinIndex(array):
    # minIdx = 0
    # for i in range(1, len(array)):
    #     if (array[minIdx] > array[i]):
    #         minIdx = i
    # return minIdx
    minIdx = 0
    for i in range(1, len(array)):
        if array[minIdx] > array[i]:
            minIdx = i
    return minIdx

## 변수
testAry = [55, 88, 33, 77, 11, 99, 100, 77, 88]


## 메인
minPos = findMinIndex(testAry)
print(testAry[minPos])