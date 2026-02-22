class Solution(object):
    def lastStoneWeight(self, stones):
        def bubble_up(heap, i):
            while i > 0:
                parent = (i - 1) // 2
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break
        
        def bubble_down(heap, i):
            n = len(heap)
            while True:
                left = 2*i + 1
                right = 2*i + 2
                largest = i
                
                if left < n and heap[left] > heap[largest]:
                    largest = left
                if right < n and heap[right] > heap[largest]:
                    largest = right
                
                if largest != i:
                    heap[i], heap[largest] = heap[largest], heap[i]
                    i = largest
                else:
                    break
        
        def push(heap, value):
            heap.append(value)
            bubble_up(heap, len(heap) - 1)
        
        def pop(heap):
            heap[0], heap[-1] = heap[-1], heap[0]
            value = heap.pop()
            if heap:
                bubble_down(heap, 0)
            return value
        heap = []
        
        # строим max-heap
        for stone in stones:
            push(heap, stone)
        
        # играем
        while len(heap) > 1:
            y = pop(heap)  # самый большой
            x = pop(heap)  # второй по величине
            
            if y != x:
                push(heap, y - x)
        
        return heap[0] if heap else 0
        