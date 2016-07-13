class Line(object):
    def __init__(self, coor1, coor2):
        # both the arguments are tuple
        # self.coor1 = coor1
        # self.coor2 = coor2
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self):
        # x1,y1 = self.coor1
        # x2,y2 = self.coor2
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())
