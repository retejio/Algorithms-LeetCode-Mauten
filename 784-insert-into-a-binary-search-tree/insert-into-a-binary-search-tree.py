class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val) #если место пустое то создаем новый узел

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val) #если значение меньше то левое поддерево
        else:
            root.right = self.insertIntoBST(root.right, val) #если значение больше то правое поддерево

        return root 

        