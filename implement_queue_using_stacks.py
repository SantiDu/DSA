class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        
    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def peek(self):
        if self.stack:
            return self.stack[-1]
    
    def pop(self):
        if self.stack:
            self.size -= 1
            return self.stack.pop()
        
    def is_empty(self):
        if self.stack:
            return False
        return True
    
class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Stack()
        self.can_push = True
        self.can_pop = False

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.can_push:
            self.queue.push(x)
        else:
            new_stack = Stack()
            while not self.queue.is_empty():
                new_stack.push(self.queue.pop())
            self.queue = new_stack
            self.can_push, self.can_pop = True, False
            self.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.can_pop:
            return self.queue.pop()
        else:
            new_stack = Stack()
            while not self.queue.is_empty():
                new_stack.push(self.queue.pop())
            self.queue = new_stack
            self.can_push, self.can_pop = False, True
            return self.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.can_pop:
            return self.queue.peek()
        else:
            new_stack = Stack()
            while not self.queue.is_empty():
                new_stack.push(self.queue.pop())
            self.queue = new_stack
            self.can_push, self.can_pop = False, True
            return self.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue.is_empty()

    
class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Stack()
        self.second_stack = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while not self.queue.is_empty():
            self.second_stack.push(self.queue.pop())
        self.queue.push(x)
        while not self.second_stack.is_empty():
            self.queue.push(self.second_stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
