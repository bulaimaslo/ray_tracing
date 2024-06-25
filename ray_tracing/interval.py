class Interval:
    def __init__(self, low=(-float('inf')), high=(float('inf'))):
        self.low = low
        self.high = high

    def size(self):
        return self.high - self.min
    
    def contains(self, x):
        return self.low <= x and self.high >= x
    
    def surrounds(self, x):
        return self.low < x and self.high > x
    
    def clamp(self, x):
        if x < self.low:
            return self.low
        elif x > self.high:
            return self.high
        else:
            return x
    
Interval.empty = Interval(float('inf'), float('-inf'))
Interval.universe = Interval(float('-inf'), float('inf'))