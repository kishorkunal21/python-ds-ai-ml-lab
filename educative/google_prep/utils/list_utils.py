from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr: list) -> Optional[ListNode]:
    """Build linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_list(head: Optional[ListNode]) -> None:
    """Print the linked list"""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def list_to_array(head: Optional[ListNode]) -> list:
    """Convert linked list back to Python list (for easy checking)"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Quick Test
if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print_list(head)
    print("As array:", list_to_array(head))