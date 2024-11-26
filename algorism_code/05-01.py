## 함수

## 변수
stack = [None,None,None,None,None]
top = -1

## 메인
print('바닥:', stack)

## push()
top += 1
stack[top] = '커피'
print('push1 바닥:', stack)

top += 1
stack[top] = '녹차'
print('push2 바닥:', stack)

top += 1
stack[top] = '꿀물'
print('push3 바닥:', stack)

##pop()
retDate = stack[top]
stack[top] = None
top -= 1

print('pop1', stack)

retDate = stack[top]
stack[top] = None
top -= 1

print('pop2', stack)

retDate = stack[top]
stack[top] = None
top -= 1

print('pop3', stack)
