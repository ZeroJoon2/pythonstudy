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