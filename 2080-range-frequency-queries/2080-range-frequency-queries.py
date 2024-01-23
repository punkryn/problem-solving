class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.hash = dict()
        for i, v in enumerate(arr):
            if v not in self.hash:
                self.hash[v] = []
            self.hash[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.hash:
            return 0
        l = bisect.bisect_left(self.hash[value], left)
        r = bisect.bisect_right(self.hash[value], right)

        return r - l
        
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)