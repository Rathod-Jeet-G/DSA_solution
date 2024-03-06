class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    temp = root
    while temp!=None :
        print(temp.data)
        temp = temp.right
        if temp==None:
            temp2 = root
            while temp2!=None:
                print(temp2.data)
                temp2 = temp2.left
                if temp2:
                    print(temp2.data)
                    temp2 = temp2.right
                    

     

main()

        