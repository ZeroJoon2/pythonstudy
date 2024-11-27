## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else :
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print(f'줄이 차서 {data}는 줄을 못서요~')
        return
    
    rear = (rear + 1) % SIZE
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

    front  = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('줄이 없는디요')
        return
    return queue[(front+1)%SIZE]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

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
retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())


enQueue('길동')
print('출구<--', queue, '<--입구')
retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())

enQueue('영준')
print('출구<--', queue, '<--입구')
retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())

enQueue('영준2')
print('출구<--', queue, '<--입구')
retData = deQueue()
print('식사 손님 : ', retData)
print('다음 손님', peek())

enQueue('영준3')
print('출구<--', queue, '<--입구')

enQueue('영준4')
print('출구<--', queue, '<--입구')

enQueue('영준5')
print('출구<--', queue, '<--입구')

enQueue('영준6')
print('출구<--', queue, '<--입구')

enQueue('영준7')
print('출구<--', queue, '<--입구')


