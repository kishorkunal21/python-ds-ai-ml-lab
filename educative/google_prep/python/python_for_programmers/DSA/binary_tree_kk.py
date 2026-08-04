#binary tree grok

from collections import deque
from typing import List

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"


class BinaryTree:
    def __init__(self):
        self.root = None


    '''
    Visual Example:
    Array = [1, 2, 3, 4, 5, None, 6]

    Step 1: Root = 1
    Step 2: 2 becomes left of 1, 3 becomes right of 1
    Step 3: 4 becomes left of 2, 5 becomes right of 2
    Step 4: 6 becomes right of 3

    This is how level-order building works.
    '''
    def build(self,nums : List[int | None] ) -> None:
        if nums[0] is None or not nums:
            self.root = None
            return

        self.root = Node(nums[0])
        queue = deque()
        queue.append(self.root)
        #[1, 2, 3, 4, 5, None, 6]

        i = 1
        while queue and i < len(nums):
            current = queue.popleft() #get root node at next level
            print('current',current.val)
            #left node
            if nums[i] is not None:
                current.left = Node(nums[i])
                queue.append(current.left)
                print('Added Left : ',current.left.val)    
            i+=1


            #right node
            if nums[i] is not None and i<len(nums):
                current.right = Node(nums[i])
                queue.append(current.right)
                print('Added right : ',current.right.val)    
            i+=1

        print('all done\n\n')


    def preorder(self):
        result = []
        
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return result
    
    def inorder(self):
            result = []
            def dfs(node):
                if node:
                    dfs(node.left)
                    result.append(node.val)
                    dfs(node.right)
            dfs(self.root)
            return result
                

    def postorder(self):
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)

        dfs(self.root)
        return result

    def print_level_nodes(self):
        dq = deque([self.root])    
        print('[',self.root.val, end=",")
        while dq:
            current = dq.popleft()
            print('')
            if current.left:
                dq.appendleft(current.left)
                print(current.left.val,end=",")
            
            if current.right:
                dq.append(current.right)
                print(current.right.val,end=",")   
        
        print(']')


    def print_tree_level_order(self):
        result = []
                
        """Print tree in level order"""
        if not self.root:
            print("Empty tree")
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result        
            


# ==================== Test ====================
if __name__ == "__main__":
    bt = BinaryTree()
    bt.build([1, 2, 3, 4, 5, None, 6])
    print("level order : ",bt.print_tree_level_order())
    print("preorder:", bt.preorder())
    print("Inorder:", bt.inorder())
    print("postorder:", bt.postorder())

    print("\n", bt.print_level_nodes())




