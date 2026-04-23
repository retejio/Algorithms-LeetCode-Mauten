class Solution(object): #РЕШЕНО ТАБУЛЯЦИЕЙ 
    def coinChange(self, coins, amount):
        #dp[i] будет хранить минимальное количество монет, необходимое для получения суммы i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0   #чтобы получить 0 нужно 0 монет
        for i in range(1, amount + 1): #проходим по всем суммам от 1 до amount 
            
            for c in coins: #для каждой суммы i пробуем использовать каждую монету
                if i - c >= 0: #проверяем можем ли мы использовать эту монету
                    
                    #если берем монету coin, то решение
                    dp[i] = min(dp[i], dp[i - c] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        