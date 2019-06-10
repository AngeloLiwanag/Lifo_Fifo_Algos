class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class stack:
    def __init__(self):
        self.head=None
    
    def push_stack(self, val):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner = newNode
        return runner.next

    def pop_stack(self):
        runner = self.head
        while (runner.next.next != None):
            runner = runner.next
        return runner.next