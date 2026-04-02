
class Solution(object):
    def preorderTraversal(self, root): # X - LEFT - RIGHT
        result = [] #сюда записываем результаты охода

        def preorder(x):
            if x is None:
                return False
            result.append(x.val) #смотрим текущи корень
            preorder(x.left) #смотрим левое поддерево
            preorder(x.right) #смотри правое поддерево
        preorder(root) #начинаем обход с корня
        return result
        