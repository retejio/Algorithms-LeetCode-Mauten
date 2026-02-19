class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0  #тот же бинарный поиск
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        #left указывает позицию вставки
        return left
