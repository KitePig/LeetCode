class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]

# Your MyHashSet object will be instantiated and called as such:
key = 120001
obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)
print(param_3)
