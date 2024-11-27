## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    
    #Case 2
    elif (rear == SIZE-1 and front==-1):
        return True
    
    #Case3 (rear = SIZE-1 and front != -1)
    elif (rear == SIZE-1 and front != -1) :
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None
        return True

    


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print(f'줄이 차서 {data}는 줄을 못서요~')
        return
    
    rear +=1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('줄에 아무도 없는디~?')
        return

    front +=1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('줄이 없는디요')
        return
    return queue[front+1]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())

retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())

retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())

retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())


enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('길동')
print('출구<--', queue, '<--입구')

enQueue('영준')
print('출구<--', queue, '<--입구')


