class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def origin(self):
        return self.origin

    def direction(self):
        return self.direction

    def at(self, t):
        return self.origin + t * self.direction
