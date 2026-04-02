class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None #если дерево пустое

        if key < root.val:
            root.left = self.deleteNode(root.left, key) #если key меньше, ищем в левом поддереве

        elif key > root.val:
            root.right = self.deleteNode(root.right, key) #если key больше, ищем в правом поддереве

        else:
            #узел найден

            if not root.left:
                return root.right #если нет левого ребенка, поднимаем правого

            if not root.right:
                return root.left #если нет правого ребенка, поднимаем левого

            #если есть оба ребенка ищем минимум в правом поддереве
            s = root.right

            while s.left:
                s = s.left #идем влево до минимального элемента

            root.val = s.val #заменяем значение текущего узла

            root.right = self.deleteNode(root.right, s.val) #удаляем

        return root 