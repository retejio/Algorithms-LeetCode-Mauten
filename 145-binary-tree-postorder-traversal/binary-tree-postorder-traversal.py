class Solution(object):
    def postorderTraversal(self, root): #LEFT - RGHT - X
        result = [] #сюда записываем результаты охода

        def postorder(x):
            if x is None:
                return False
            postorder(x.left) #смотрим левое поддерево
            postorder(x.right) #смотри правое поддерево
            result.append(x.val) #смотрим текущи корень
        postorder(root) #начинаем обход с корня
        return result   