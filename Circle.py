class Circle:

    pie = 3.14 # static variable, class variables

    def __init__(self, radius):
        self.radius = radius
        # self.pie = 3.14

    # wrong
    #def printPieWithStars(self):
    #    print(f'**** {Circle.pie} ****')

    @staticmethod
    def modify_pie(new_pie):
        Circle.pie = new_pie

    @staticmethod
    def printradiusWithStars(circle):
        print(f'**** {circle.radius} ****')

    @staticmethod
    def printPieWithStars():
        print(f'**** {Circle.pie} ****')
        # print(self.radius) # wrong

    def getArea(self):
        # return self.pie * self.radius ** 2
        # pie = 3.14          # function variable
        # self.pie = 3.14     # object member
        # Circle.pie = 3.14   # class variable
        return Circle.pie * self.radius ** 2

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)