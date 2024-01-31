class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self. email = email
        self.customer_id = Customer.next_id()
        self.id = self.customer_id

    @classmethod
    def next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Customer.id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"
