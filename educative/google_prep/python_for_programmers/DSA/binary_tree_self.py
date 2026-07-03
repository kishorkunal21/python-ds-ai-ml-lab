from typing import List,Optional
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self ):
        self.root = None

    def build(self, values:List[int | None])-> Node | None:
        pass
        # for v in values:           

        #     new_node  = Node(value = v)

        #     if self.root == None :
        #         self.root == new_node
        #     else:
        #         #10,5,30
        #         if self.root.value > v:
        #             self.root.right = Node(v)
        #         else:
        #             self.root.left = Node(v)        
        