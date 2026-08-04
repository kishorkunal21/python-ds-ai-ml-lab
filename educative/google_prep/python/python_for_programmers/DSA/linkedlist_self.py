class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None #next node 


class LinkedList:
    def __init__(self):
        self.head = None ##first node empty


    def append(self,data):
        new_node = Node(data=data)

        ## list is empty
        if self.head is None:
            self.head = new_node
            return

        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, data, after):
        new_node = Node(data=data)
        current_node = self.head
        # 40 - 10 - 20 - 30 : 100 after 20
        while current_node.next is not None:
            print(f"current : {current_node.data} after : {after}")
            if after == current_node.data:
                temp_next = current_node.next
                current_node.next = new_node
                new_node.next = temp_next
                return
            else:
                current_node = current_node.next


    def delete_node(self, delete_node):
        if self.head is not None:
            if self.head.data == delete_node:
                self.head = self.head.next
                return
            else:
                prev_node = self.head
                current_node = self.head.next
                while current_node.next is not None:
                    if current_node.data == delete_node:
                        prev_node.next = current_node.next
                        current_node = None
                        return
                    else:
                        prev_node = current_node
                        current_node = current_node.next

    def delete_by_position(self, position):
        if position == 0:
            self.head = self.head.next
            return
        current_position = 1
        prev_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            if current_position == position:
                prev_node.next = current_node.next
                current_node = None
                return
            else:
                current_position += 1 
                prev_node = current_node
                current_node = current_node.next   

    def length(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.length(node=node.next)


                        

    def display_list(self):
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                print(current_node.data,end = " -> ")
                current_node = current_node.next
            print(current_node.data)    

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.display_list()      
    linked_list.prepend(40)          
    linked_list.display_list()  
    linked_list.insert_after(100,20)
    linked_list.display_list()
    linked_list.delete_node(100)
    linked_list.display_list()
    linked_list.delete_by_position(2)
    linked_list.display_list()  
    print(linked_list.length(linked_list.head))





