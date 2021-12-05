from datetime import datetime

class Customer:

    # static member
    current_id = 1

    # *etgar
    last_customer_creation_time = None

    def __init__(self, fname, lname):
        self.id = Customer.current_id
        Customer.current_id += 1
        self.fname = fname
        self.lname = lname
        Customer.last_customer_creation_time = datetime.now()

    @staticmethod
    def when_was_last_created():
        return Customer.last_customer_creation_time

    @staticmethod
    def get_current_id():
        return Customer.current_id

    @staticmethod
    def reset_id():
        Customer.current_id = 1

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)