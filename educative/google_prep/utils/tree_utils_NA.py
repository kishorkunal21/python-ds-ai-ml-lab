from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

def print_tree(root: Optional[TreeNode]) -> None:
    """Clear tree with Left/Right labels"""
    if not root:
        print("Empty tree")
        return

    def helper(node, prefix="", is_left=True):
        if node is None:
            return
        
        side = "Left" if is_left else "Right"
        print(prefix + ("├── " if is_left else "└── ") + f"{side}: {node.val}")
        
        new_prefix = prefix + ("│   " if is_left else "    ")
        
        helper(node.left, new_prefix, True)
        helper(node.right, new_prefix, False)

    print("Tree Structure:")
    helper(root)

# Quick Test
if __name__ == "__main__":
    root = build_tree([1,2,3,4,5,None,6])
    print_tree(root)