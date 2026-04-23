class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]  #если один дом

        dp = [0] * len(nums)  #массив для хранения результатов
        dp[0] = nums[0]       #первый дом
        dp[1] = max(nums[0], nums[1])  #лучший из первых двух

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])  #либо не берем текущий либо берем

        return dp[-1]
        