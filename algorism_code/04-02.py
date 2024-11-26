## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(head):
    current = head
    print(current.data , end = '\t')


    while (current.link != None):
        current = current.link
        print(current.data, end = '\t')

    print()
# def insertNode(findData, insertData):
#     global memory, head, current, pre
    
#     # Case1. header 앞에 삽입
#     if head.data == findData :
#         node = Node()
#         node.data = insertData
#         node.link = head
#         head = node

#     # Case2. 찾는 애가 중간에 있을 때,
#     current = head
#     while (current.link != None):
#         pre = current
#         current = current.link
#         if (current.data == findData):
#             node = Node()
#             node.data = insertData
#             node.link = current
#             pre.link = node
#             return
        
#     # Case3. 찾는 애가 없을때
#     node = Node()
#     node.data = insertData #append 느낌
#     current.link = node
#     return

def insertNode(findData, insertData):
    global head, current, pre

    # Case1 제일 앞에 있을때
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # Case2 중간에 있을때
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    # Case3 찾는 것이 없을때
    node = Node()
    node.data = insertData
    current.link = node
    return


# def deleteNode(deleteData):
#     global head, current, pre
    
#     # Case1 머리를 삭제할때
#     if head.data == deleteData:
#         current = head
#         head = head.link
#         del(current)
#         return
    
#     # Case2 중간 내용 삭제
#     current = head
    
#     while (current.link is not None):
#         pre = current
#         current = current.link
#         if current.data == deleteData:
#             pre.link = current.link
#             del (current)
#             return
        
#     # Case3 지울 데이터가 없을때
#     return

def deleteNode(deleteData):
    global head, pre, current

    # 찾는게 헤드 일때
    if head.data == deleteData:
        current = head
        head = current.link
        del(current)
        return
    
    # 찾는게 중간에 있을 때,
    current = head
    while head.link is not None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del current
            return
        
    # Case 3 지울 데이터가 없음
    return

def findNode(findData):
    global head, current, pre
    current = head
    if (current.data == findData):
        return current
    while current.link != None:
        current = current.link
        if (current.data == findData):
            return current
        
    return Node() #빈 로드 반환해줌

## 변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

## 메인
# node = Node()
# node.data = dataArray[0]
# head = node
# memory.append(node) # 생략가능

# for data in dataArray[1:]:
#     pre = node
#     node = Node()
#     node.data = data
#     pre.link = node
#     memory.append(node) # 생략 가능


node = Node()
node.data = dataArray[0]
head = node

for i in dataArray[1:]:
    pre = node
    node = Node()
    node.data = i
    pre.link = node

printNodes(head)

# insertNode('다현', '화사')
insertNode('사나','솔라')
printNodes(head)

insertNode('영준','영준2')
printNodes(head)

deleteNode('다현')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

deleteNode('영준2')
printNodes(head)

retNode = findNode('사나')
print(retNode.data,'의 뮤비가 나옵니다~')