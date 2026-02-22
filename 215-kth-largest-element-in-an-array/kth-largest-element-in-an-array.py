class Solution(object):
    def findKthLargest(self, nums, k):

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        n = len(nums)

        #build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        #извлекаем максимум k-1 раз
        for i in range(n - 1, n - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums[0]