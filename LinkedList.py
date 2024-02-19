class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    


    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1

        if self.length == 0: 
            self.tail = None

        return temp


    def pop(self):
        if self.head is None:
            return None
        
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    

    def get(self, index):
        if index > self.length or index < 0:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp


    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        previous = self.get(index - 1)
        new_node.next = previous.next
        previous.next = new_node
        self.length += 1
        return True
    

    def remove(self, index):
        if index > self.length or index < 0:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next 
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        prev = None

        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after


    def find_middle_node(self):
        slow = self.head
        fast = slow
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


    def has_loop(self):
        slow = self.head
        fast = slow
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    

    def find_kth_from_end(self, k):
        if k <= 0:
            return None
        
        slow = self.head
        fast = slow
        
        for _ in range(k):
            if not fast:
                return None
            fast = fast.next
                
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow


    def remove_duplicates(self):
        existing = set()
        previous = None
        current = self.head
        
        while current:
            if current.value in existing:
                previous.next = current.next
                self.length -= 1
            else:
                existing.add(current.value)
                previous = current
            current = current.next


    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num
    

    def reverse_between(self, start_index, end_index):
        if not self.head or self.length <= 1:
            return None
        
        dummy = Node(0)
        
        dummy.next = self.head
        previous_node = dummy
        
        for _ in range(start_index):
            previous_node = previous_node.next
            
        current = previous_node.next
        
        for _ in range(end_index - start_index):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
            
        self.head = dummy.next   