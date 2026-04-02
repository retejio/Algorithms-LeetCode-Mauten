class Solution(object):
    def inorderTraversal(self, root): #LEFT - X - RIGHT
        result = [] #сюда записываем результаты охода

        def inorder(x):
            if x is None:
                return False
            inorder(x.left) #смотрим левое поддерево
            result.append(x.val) #смотрим текущи корень
            inorder(x.right) #смотри правое поддерево
        inorder(root)
        return result