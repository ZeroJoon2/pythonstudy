## 함수
def isStackFull():
    global SIZE, stack, top
    if (top == SIZE - 1):
        return True
    else:
        return False


def push(data):
    global SIZE, stack, top
    if isStackFull() == True:
        print(f'''
              *******************
              full~
              ''')
    else:
        top += 1
        stack[top] = data
        print(f'{data} add success~')
def isStackEmpty():
    global SIZE, stack, top

    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택이 비었음')
        return 
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack,top
    if (isStackEmpty()):
        print('스택 비었음')
        return
    return stack[top]

## 변수
SIZE = 5
stack = [None for i in range(SIZE)]
top = -1
print(stack)


## 메인
push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
push('게토레이')
print('바닥 : ', stack)

retData = pop()
print('pop', retData)

print('**다음 나올 예정',peek())