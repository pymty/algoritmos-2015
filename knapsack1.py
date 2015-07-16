class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
 
    def __str__(self):
        return "Value: %d - Weight: %d" % (self.value, self.weight)
    
    def __repr__(self):
        return self.__str__()


def ks(items, capacity):
    if not items:
        return 0
 
    item = items[0]
 
    if item.weight > capacity:
        return ks(items[1:], capacity)
    else:
        return max(ks(items[1:], capacity),
                   ks(items[1:], capacity - item.weight) + item.value)
 
items = [Item(1, 15), Item(4, 12), Item(2, 2), Item(2, 1), Item(1, 1), Item(10, 4)]
print "Max sum: %d" % (ks(items, 20),)