class Solution:
    def isValidBST(self, root): #LEFT → x → RIGHT
        values = []

        def inorder(x):  #x - узел
            if not x:
                return
            
            inorder(x.left) #обход левого поддерева
            values.append(x.val) #добавляем текущий узел
            inorder(x.right) #обход правого поддерева

        inorder(root)

        #проверяем что последовательность строго возрастает
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False

        return True