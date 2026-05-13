class User:
# user don't have an id until they are saved to the database
# so we need a default value for id
# and parameters with a default must come last
# this change, means the `BookRepository` will no longer work as expected
    def __init__(self, username, password, id = None):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

        # This method makes it look nicer when we print a Book
    def __repr__(self):
        return f"Book({self.id}, {self.username}, {self.password})"
