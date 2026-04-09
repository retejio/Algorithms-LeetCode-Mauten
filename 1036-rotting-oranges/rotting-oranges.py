from collections import deque

class Solution(object):
    def orangesRotting(self, grid):

        rows = len(grid) #количество строк
        cols = len(grid[0]) #количество столбцов

        queue = deque() #очередь для BFS, сюда кладем гнилые апельсины
        f = 0 #количество свежих апельсинов

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j)) #все гнилые сразу кладем в очередь
                elif grid[i][j] == 1:
                    f += 1 #считаем свежие

        time = 0 #счетчик времени

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #4 направления

        while queue and f > 0:
            for _ in range(len(queue)): #обрабатываем один уровень BFS
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 #делаем апельсин гнилым
                        f -= 1 #уменьшаем количество свежих
                        queue.append((nr, nc)) #добавляем в очередь

            time += 1 #прошла одна минута

        if f > 0: #если остались свежие то значит их невозможно заразить
            return -1

        return time