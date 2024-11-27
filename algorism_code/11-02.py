## 함수
import random
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx


## 변수
before = [random.randint(30, 198) for _ in range(8)]
after = []

## 메인
print(before)
for i in range(0, len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    print(before[minPos])
    del(before[minPos])


print(after)