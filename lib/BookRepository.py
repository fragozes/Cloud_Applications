from lib.Book import Books

class BooksRepository():
    def __init__(self, connection):
        self._connection = connection
    

    # Selecting all records
    # No arguments
        # id is now the third argument
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Books(row["title"], row["author"], row["id"])
            books.append(item)
        return books

    
    #Create a new book
    def create_book(self, book):
        self._connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)',
                                [book.title, book.author])
        return None

