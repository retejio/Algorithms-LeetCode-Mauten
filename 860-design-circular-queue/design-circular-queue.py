class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0] * k#массив фиксированного размера
        self.size = k#максимальный размер очереди
        self.front = 0#индекс первого элемента
        self.rear = -1#индекс последнего элемента
        self.count = 0#текущее количество элементов

    def enQueue(self, value):
        if self.isFull():
            return False#если очередь заполнена
        
        self.rear = (self.rear + 1) % self.size#циклический переход
        self.queue[self.rear] = value#вставка элемента
        self.count += 1#увеличиваем количество элементов
        
        return True

    def deQueue(self):
        if self.isEmpty():
            return False#если очередь пустая
        
        self.front = (self.front + 1) % self.size#сдвигаем front
        self.count -= 1#уменьшаем количество элементов
        
        return True

    def Front(self):
        if self.isEmpty():
            return -1#если очередь пустая
        
        return self.queue[self.front]#первый элемент

    def Rear(self):
        if self.isEmpty():
            return -1#если очередь пустая
        
        return self.queue[self.rear]#последний элемент

    def isEmpty(self):
        return self.count == 0#очередь пуста

    def isFull(self):
        return self.count == self.size#очередь заполнена