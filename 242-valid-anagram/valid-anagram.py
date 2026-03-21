class Solution(object):
    def isAnagram(self, s, t):
        hashmap = {}
        hashmap2 = {}
        if len(s)!=len(t):
            return False
        for char in s:
            if char in hashmap:
                hashmap[char] += 1 #еслим буква есть увеличиваем счетчик
            else:
                hashmap[char] = 1 #если нету то инициалиизрукем как 1
        for char in t:
            if char in hashmap2:
                hashmap2[char] += 1
            else:
                hashmap2[char] = 1 
        return hashmap == hashmap2