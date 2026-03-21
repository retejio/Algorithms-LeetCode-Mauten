class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = {}

        for i in nums:
            if i in hashmap:
               return True
            hashmap[i] = True #проверяем встречалось ли число если не встречалось то запоминаем его

        return False