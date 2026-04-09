import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = {} #список смежности для хранения графа

        for i in range(1, n + 1):
            graph[i] = [] #для каждой вершины создаем пустой список соседей

        for start, end, weight in times:
            graph[start].append((end, weight)) #из start можно попасть в end с весом weight

        distance = {} #словарь для хранения минимальных расстояний

        for i in range(1, n + 1):
            distance[i] = float('inf') #сначала до всех вершин расстояние бесконечность

        distance[k] = 0 #до стартовой вершины расстояние равно 0

        heap = [(0, k)] #приоритетная очередь (текущее расстояние, вершина)

        while heap:
            current_dist, current_node = heapq.heappop(heap) #берем вершину с минимальным расстоянием

            for neighbor, weight in graph[current_node]: #просматриваем всех соседей текущей вершины
                if distance[neighbor] > distance[current_node] + weight: #если найден более короткий путь
                    distance[neighbor] = distance[current_node] + weight #обновляем расстояние
                    heapq.heappush(heap, (distance[neighbor], neighbor)) #добавляем новую вершину в очередь

        answer = max(distance.values()) #максимальное расстояние среди всех вершин

        if answer == float('inf'): #если хотя бы одна вершина недостижима
            return -1

        return answer