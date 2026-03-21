class Solution(object):
    def intersection(self, nums1, nums2):
        hashmap = {}
        result = []

        for i in nums1:
            hashmap[i] = True #запоминаем все уникальные элементы первого массива

        for i in nums2:
            if i in hashmap: #если элемент есть в первом массиве
                result.append(i)
                del hashmap[i] #удаляем чтобы не было повторов

        return result