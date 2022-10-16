class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asphalt_calculation(self, weight, thickness):
        return self.length * self.width * weight * thickness / 1000


example = Road(20, 5000)
print(example.asphalt_calculation(25, 5))
