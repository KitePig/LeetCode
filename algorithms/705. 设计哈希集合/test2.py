class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 1000
        self.set = [[]] * self.bucket # 创建定长拉链数组

    def hash(self, key):
        return key % self.bucket

    def add(self, key: int) -> None:
        hash_key = self.hash(key)
        if key in self.set[hash_key]:
            return
        self.set[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if key not in self.set[hash_key]:
            return
        self.set[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = self.hash(key)
        return key in self.set[hash_key]



# Your MyHashSet object will be instantiated and called as such:
key = 222
obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)
print(param_3)
