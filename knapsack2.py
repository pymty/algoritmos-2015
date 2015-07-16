class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
 
    def __str__(self):
        return "Value: %d - Weight: %d" % (self.value, self.weight)
    
    def __repr__(self):
        return self.__str__()

items = [Item(1, 15), Item(4, 12), Item(2, 2), Item(2, 1), Item(1, 1), Item(10, 4)]

def memoization(fun):
    mem = {}
    def wrapper(*args):
        if args not in mem:
            mem[args] = fun(*args)
        return mem[args]
    return wrapper

@memoization
def ks(index, capacity):
    if index >= len(items):
        return 0
 
    item = items[index]
 
    if item.weight > capacity:
        return ks(index+1, capacity)
    else:
        return max(ks(index + 1, capacity),
                   ks(index + 1, capacity - item.weight) + item.value)
 

print "Max sum: %d" % (ks(0, 20),)
