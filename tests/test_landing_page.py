from playwright.sync_api import Page, expect

def test_create_new_book(page: Page):
    page.goto("http://127.0.0.1:5002/books")
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