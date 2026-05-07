from lib.Book import Books

class BooksRepository():
    def __init__(self, connection):
        self._connection = connection
    

    # Selecting all records
    # No arguments
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Books(row["id"],
                        row["title"], 
                        row["author_name"])
            books.append(item)
        return books
