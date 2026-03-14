class Solution(object):
    def evalRPN(self, tokens):
        stack = []#стек для хранения чисел
        
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))#если число то добавляем в стек
            else:
                b = stack.pop()#второй операнд
                a = stack.pop()#первый операнд #сначала идет второй операнд чтобы при вычитании не произошло логических ошибок
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(float(a) / b))
        
        return stack[0]
        