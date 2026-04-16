import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n  #массив для отслеживания уже добавленных вершин в дерево
        min_dist = [float('inf')] * n  #минимальная стоимость до каждой вершины
        min_dist[0] = 0  #начинаем с 0
        pq = [(0, 0)]  #очередь с приоритетом (стоимость, вершина)

        result = 0  #стоимость

        while pq:
            cost, u = heapq.heappop(pq)  #берем вершину с минимальным весом
            if visited[u]:
                continue  

            visited[u] = True  #добавляем вершину в дерево
            result += cost  

            for v in range(n):
                if not visited[v]:
                    #считаем манхэттенское расстояние
                    weight = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])

                    if weight < min_dist[v]:
                        min_dist[v] = weight  #обновляем минимальное ребро для вершины
                        heapq.heappush(pq, (weight, v))  #добавляем в очередь

        return result