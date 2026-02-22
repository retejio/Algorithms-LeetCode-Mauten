class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #считаем частоту
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = [] #min-heap
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k: #если элементов больше k — удаляем наименьшую частоту
                heapq.heappop(heap)
        
        return [num for count, num in heap]