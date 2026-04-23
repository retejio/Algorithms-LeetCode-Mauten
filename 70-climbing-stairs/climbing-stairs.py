class Solution(object):
    def climbStairs(self, n):
        if n == 1: #базовые случаи
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)  #массив для хранения результатов
        dp[1] = 1 #начальные значения
        dp[2] = 2
        
        for i in range(3, n + 1): #заполняем массив снизу вверх
            dp[i] = dp[i - 1] + dp[i - 2]  
        
        return dp[n]