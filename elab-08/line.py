class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.slope = (y2 - y1) / (x2 - x1)
        self.y_intercept = -self.slope * x1 + y1
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)

    def contains(self, x, y):
        if y == self.slope * x + self.y_intercept and self.x1 <= x <= self.x2:
            return True
        return False

    def get_distance(self):
        return ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    def get_y(self, x):
        if self.x1 <= x <= self.x2:
            return self.slope * x + self.y_intercept
        return -999.999


class Point:
    # Constuctor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_on_x_axis(self):
        if self.__y == 0:
            return True
        else:
            return False

    def is_on_y_axis(self):
        if self.__x == 0:
            return True
        else:
            return False

    def translate(self, dist_x, dist_y):
        self.__x = self.__x + dist_x
        self.__y = self.__y + dist_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
