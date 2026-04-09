class Solution(object):
    def numIslands(self, grid):
        if not grid: #если таблица пустая
            return 0

        rows = len(grid) #количество строк
        cols = len(grid[0]) #количество столбцов

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: #если вышли за границы
                return

            if grid[r][c] != "1": #если это вода или уже посещенная клетка
                return

            grid[r][c] = "0" #помечаем землю как посещенную

            dfs(r + 1, c) #идем вниз
            dfs(r - 1, c) #идем вверх
            dfs(r, c + 1) #идем вправо
            dfs(r, c - 1) #идем влево

        count = 0 #счетчик 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1": #если нашли новую землю
                    count += 1 #нашли новый остров
                    dfs(row, col) #обходим весь остров

        return count
        