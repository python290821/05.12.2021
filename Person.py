class Person:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name # name must be at least 4 characters
        self.__age = age # PRIVATE
        self.__temperature = 90

    def set_age(self, new_age):
        if (new_age < 0):
            print('negative age is invalid. I am not changing!!!!')
            return
        self.__age = new_age

    # getter - gets a private attribute value interpreted
    def get_temprature(self):
        # check region -- F or C
        return None

    # getter - gets a private attribute value
    def get_age(self):
        return self.__age

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)