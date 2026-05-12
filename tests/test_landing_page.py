from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("http://0.0.0.0:5001")

#     h1 = page.locator("h1")

#     expect(h1).to_have_text("Welcome to AceReads Test")

# def test_has_title_book(page: Page):
#     page.goto("http://127.0.0.1:5001/books_html")

#     h1 = page.locator("h1")

#     expect(h1).to_have_text("My Books")

# #ou don't need to iterate through all the li elements. 
# # Playwright has a handy method you can use instead.
# def test_book_list_contains_all_books(page: Page): 
#     page.goto("http://127.0.0.1:5001/books_html") 

#     books = page.locator('li') 

#     expected_books = [ 
#     'The Gruffalo by Julia Donaldson', 
#     'Ada Twist, Scientist by Andrea Beaty', 
#     'The Girl Who Drank the Moon by Kelly Barnhill', 
#     'Dragons in a Bag by Zetta Elliott' 
#     ] 

#     # here's the neat part which saves you from iterating over the `li` elements 
#     actual_books = books.all_inner_texts() 

#     assert actual_books == expected_books

def test_create_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"

from lib.DatabaseConnection import *
#Using seeds file
def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/book.sql")

    # the rest is unchanged