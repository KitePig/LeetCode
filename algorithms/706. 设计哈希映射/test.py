class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 987 #用质数桶分布会均匀一些
        self.table = [[]] * self.bucket

    def hash_key(self, key):
        return key % self.bucket #取模/分组

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = self.hash_key(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hash_key].append([key, value])
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self.hash_key(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self.hash_key(key)
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                self.table[hash_key].pop(i)
                return
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
