class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows = len(image) #количество строк
        cols = len(image[0]) #количество столбцов   

        base_color = image[sr][sc] #запоминаем исходный цвет стартовой клетки

        if base_color == color: #если цвет уже такой же, менять ничего не нужно
            return image

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: #если вышли за границы массива
                return

            if image[r][c] != base_color: #если цвет клетки не совпадает с исходным
                return

            image[r][c] = color #перекрашиваем текущую клетку

            dfs(r + 1, c) #идем вниз
            dfs(r - 1, c) #идем вверх
            dfs(r, c + 1) #идем вправо
            dfs(r, c - 1) #идем влево

        dfs(sr, sc) #запускаем обход 
        return image