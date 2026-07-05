from utils.tree_utils import BinaryTree


bt  = BinaryTree()
bt.build_from_list([1,2,3,4,4,5])
bt.print_tree(bt.root)