from collections import deque
from typing import List

class Node:
    """Represents a single node in the Binary Tree"""
    def __init__(self, val: int = 0, left: 'Node' | None = None, right: 'Node' | None = None):
        self.val = val          # Value stored in this node
        self.left = left        # Reference to left child
        self.right = right      # Reference to right child


class BinaryTree:
    """Main class to manage the entire Binary Tree"""
    
    def __init__(self):
        self.root: Node | None = None   # Root of the tree (starts as empty)

    def build_from_list(self, arr: List[int | None]) -> None:
        """
        Build a binary tree from a level-order list.
        Example: [1, 2, 3, 4, 5, None, 6]
        None means no node at that position.
        """
        if not arr or arr[0] is None:
            self.root = None
            return
        
        # Create root node
        self.root = Node(arr[0])
        queue = deque([self.root])   # Queue to help build level by level
        i = 1                        # Index to track position in array
        
        while queue and i < len(arr):
            current = queue.popleft()   # Process next node
            
            # Assign Left Child
            if i < len(arr) and arr[i] is not None:
                current.left = Node(arr[i])
                queue.append(current.left)
            i += 1
            
            # Assign Right Child
            if i < len(arr) and arr[i] is not None:
                current.right = Node(arr[i])
                queue.append(current.right)
            i += 1

    def print_tree(self) -> None:
        """Print the tree in Level Order (BFS)"""
        if not self.root:
            print("Empty tree")
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def inorder(self) -> List[int]:
        """Inorder Traversal: Left -> Root -> Right"""
        result: List[int] = []
        def dfs(node: Node | None):
            if node:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(self.root)
        return result

    def preorder(self) -> List[int]:
        """Preorder Traversal: Root -> Left -> Right"""
        result: List[int] = []
        def dfs(node: Node | None):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return result

    def postorder(self) -> List[int]:
        """Postorder Traversal: Left -> Right -> Root"""
        result: List[int] = []
        def dfs(node: Node | None):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.val)
        dfs(self.root)
        return result


# ==================== Test the class ====================
if __name__ == "__main__":
    bt = BinaryTree()
    bt.build_from_list([1, 2, 3, 4, 5, None, 6])
    
    print("Level Order:")
    bt.print_tree()
    
    print("Inorder Traversal:", bt.inorder())
    print("Preorder Traversal:", bt.preorder())
    print("Postorder Traversal:", bt.postorder())