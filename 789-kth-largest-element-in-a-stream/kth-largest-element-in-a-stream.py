class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        
        # Превращаем список в min-heap
        heapq.heapify(self.heap)
        
        # Оставляем только k наибольших элементов
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Добавляем новый элемент в кучу
        heapq.heappush(self.heap, val)
        
        # Если элементов стало больше k — удаляем минимальный
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Минимальный в куче — это k-й наибольший
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)