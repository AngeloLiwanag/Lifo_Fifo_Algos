class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        current = self.head
        node = SLNode(val)
        node.next = current
        self.head = node
    
    def pop(self):
        temp = self.head.val
        self.head = self.head.next
        return temp 