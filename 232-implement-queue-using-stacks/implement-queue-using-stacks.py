class MyQueue(object):

    def __init__(self):
        self.stack1 = []#стек для добавления
        self.stack2 = []#стек для удаления

    def push(self, x):
        self.stack1.append(x)#добавляем элемент в stack1

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())#переносим элементы в обратном порядке
        
        return self.stack2.pop()#удаляем первый элемент очереди

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())#переносим элементы
        
        return self.stack2[-1]#смотрим первый элемент очереди

    def empty(self):
        return not self.stack1 and not self.stack2#очередь пуста если оба стека пустые