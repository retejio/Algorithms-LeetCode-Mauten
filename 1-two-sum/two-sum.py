class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {} #хэш таблица для хранения числа и индекса 

        for i in range(len(nums)): #проходимся по массиву и ищем к каждому числу число которое нужно чтобы дало таргет
            s = target - nums[i] #нужное числло

            if s in hashmap: #если нужное число уже встречалось то задача решена 
               return [hashmap[s], i]

            hashmap[nums[i]]=i #если же нет то запоминаем число и записывваем в в хэш таблицу