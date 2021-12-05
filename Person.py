class Person:

    def __init__(self, id, name, age):
        self.id = id
        self.__name = name # name must be at least 4 characters
        self.__age = age # PRIVATE
        self.__temperature = 90

    def set_name(self, new_name):
        if len(new_name) < 4:
            print('too short! dahh')
            return
        self.__name = new_name

    def get_name(self):
        return self.__name

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
        return f'Person id:{self.id} name:{self.__name} age: {self.__age}'

    def __repr__(self):
        return str(self.__dict__)