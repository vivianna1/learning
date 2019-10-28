class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)   #初始化fromkeys

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

    # c1 = CoumtList(1,3,5,7,9)
    # c2 = CountList(2,4,6,8,10)
    # c1[1]
    # c2[1]
    # c1[1] + c2[1]
    # c1.count
    #{0:0, 1:2, 2:0, 3:0 4:0}