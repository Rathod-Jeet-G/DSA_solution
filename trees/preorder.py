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
        root.left.right.left = Node(6)
        root.right = Node(3)
        root.right.left = Node(7)
        root.right.right = Node(8)
        root.right.right.left = Node(9)
        root.right.right.right = Node(10)
        return root
    
    def preorder(self,root):
        if root == None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inoreder(self,root):
        if root == None:
            return
        self.inoreder(root.left)
        print(root.data)
        self.inoreder(root.right)
    
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

def main():
    t = Tree()
    # taking root node    
    root_node= t.tree()

    print("preorder traverser:")
    t.preorder(root_node)

    print("inorder traverser:")
    t.inoreder(root_node)
    
    print("postoreder traverser:")
    t.postorder(root_node)

main()

