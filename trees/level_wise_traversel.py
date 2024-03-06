from collections import deque
class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(7)
        return root
    def levelWise(self,root):
        ans = []
        if root is None:
            return ans
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()
               
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                level.append(node.data)
            ans.append(level)
        print(ans)


def main():
    t = Tree()
    # taking root node    
    root_node= t.tree()

    t.levelWise(root_node)


main()

