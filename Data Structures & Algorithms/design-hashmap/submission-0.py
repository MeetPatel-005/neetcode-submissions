class MyHashMap:

    def __init__(self):
        self.hash_ = []

    def put(self, key: int, value: int) -> None:
        for x in self.hash_:
            if key == x[0]:
                x[1] = value
        else: self.hash_.append([key,value]) 

    def get(self, key: int) -> int:
        for x in self.hash_:
            if key == x[0]:
                return x[1]
        else: return -1

    def remove(self, key: int) -> None:
       for x in self.hash_:
            if key == x[0]:
                x[1] = -1 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)