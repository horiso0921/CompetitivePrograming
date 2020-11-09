class Dice:
    __slots__ = ["data"]
    state = ["top", "front", "right", "left", "back", "bottom"]
    index = {c:i for i,c in enumerate(state)}
 
    def __init__(self, data=list(range(1,7))):
        self.data = data[:]
    
    def __getitem__(self, key):
        if type(key) is int:
            return self.data[key]
        else:
            return self.data[self.index[key]]

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data
    
    def __ne__(self, other):
        return self.data != other.data
    
    def move_front(self):
        self.data = [self.data[4], self.data[0], self.data[2], self.data[3], self.data[5], self.data[1]]
        
    def move_back(self):
        self.data = [self.data[1], self.data[5], self.data[2], self.data[3], self.data[0], self.data[4]]

    def move_left(self):
        self.data = [self.data[2], self.data[1], self.data[5], self.data[0], self.data[4], self.data[3]]
    
    def move_right(self):
        self.data = [self.data[3], self.data[1], self.data[0], self.data[5], self.data[4], self.data[2]]
        
    def turn_left(self):
        self.data = [self.data[0], self.data[2], self.data[4], self.data[1], self.data[3], self.data[5]]

    def turn_right(self):
        self.data = [self.data[0], self.data[3], self.data[1], self.data[4], self.data[2], self.data[5]]

    def all(self):
        tmp = Dice(self.data)
        for i in range(24):
            yield tmp
            tmp.turn_right()
            if i&7 == 7:
                tmp.move_back()
            elif i&3 == 3:
                tmp.move_right()

def main():
    n1 = [int(i) for i in input().split()]
    n2 = [int(i) for i in input().split()]
    d1 = Dice(n1)
    d2 = Dice(n2)
    for d in d1.all():
        if d == d2:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()
    