class Solution(object):
    def isValid(self, s):
        stack = [] # создаем стек для хранения открывающих скобок
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in '([{':
                stack.append(char) #добавляем открывающую скобку
            else:
                if not stack:
                    return False #если стек пуст а скобка закрывающая
                
                top = stack.pop() #берем последнюю открытую скобку
                
                if top != pairs[char]:
                    return False  #если тип скобок не совпадает
        
        return len(stack) == 0  #если стек пуст, значит всё корректно