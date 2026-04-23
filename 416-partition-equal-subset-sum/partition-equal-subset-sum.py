class Solution(object): #
    def canPartition(self, nums):
        total = sum(nums) #общая сумма массива
        
        if total % 2 != 0: #если сумма нечетная то нельзя разбить на 2 равные части
            return False
        goal = total // 2 #целевая сумма это четное число и тогда можно поделить на равные части
        
        dp = [False] * (goal + 1) #можно ли набрать сумму i
        dp[0] = True #сумму 0 всегда можно набрать
        
        for num in nums:
            for i in range(goal, num - 1, -1): #идем с конца чтобы не переиспользовать один и тот же элемент несколько раз
                if dp[i - num]:
                    dp[i] = True
        return dp[goal]
        