class MinStack(object):

    def __init__(self):
        self.stack = [] #основной стек
        self.min_stack = [] #второй стек

    def push(self, val):
        self.stack.append(val) #добавляем элемент в основной стек
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) #если элемент меньше текущего минимума, добавляем его
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop() #удаляем верхний элемент из основного стека
        self.min_stack.pop() #удаляем верхний минимум

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]