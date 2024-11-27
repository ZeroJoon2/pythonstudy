## 함수 클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'

node1.left = node2.data

node3 = TreeNode()
node3.data = '문별'

node1.right = node3.data


node4 = TreeNode()
node4.data = '휘인'

node5 = TreeNode()
node5.data = '쯔위'

node6 = TreeNode
node6.data = '선미'


node2.left = node4.data
node2.right = node5.data
node3.left = node6.data

root = node1

print(node1.data)
print(node2.data, node3.data)
print(node4.data, node5.data, node6.data)

print("*********")
print(node1.data)
print(node1.left, node1.right)
print(node2.left, node2.right, node3.left)

print("*********")
print(root.data)
print(root.left, root.right)
#print(root.left.left.data, root.right)
#print(root.left.left.data, root.left.right.data, root.right.left.data)


## 메인