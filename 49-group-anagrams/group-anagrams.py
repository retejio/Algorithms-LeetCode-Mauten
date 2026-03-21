class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}

        for i in strs:
            key = ''.join(sorted(i)) #сортируем буквы в слове и соединяем их обратно в строку чтобы у анаграмм получился одинаковый ключ

            if key in hashmap:
                hashmap[key].append(i) #если такой ключ уже есть в словаре значит найдено слово с таким же набором букв и добавляем его в эту группу
            else:
                hashmap[key] = [i] #если такого ключа еще нет создаем новую группу и помещаем туда слово

        return hashmap.values() 