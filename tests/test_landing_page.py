from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Welcome to AceReads")

def test_has_title_book(page: Page):
    page.goto("http://127.0.0.1:5001/books_html")

    h1 = page.locator("h1")

    expect(h1).to_have_text("My Books")

#ou don't need to iterate through all the li elements. 
# Playwright has a handy method you can use instead.
def test_book_list_contains_all_books(page: Page): 
    page.goto("http://127.0.0.1:5001/books_html") 

    books = page.locator('li') 

    expected_books = [ 
    'The Gruffalo by Julia Donaldson', 
    'Ada Twist, Scientist by Andrea Beaty', 
    'The Girl Who Drank the Moon by Kelly Barnhill', 
    'Dragons in a Bag by Zetta Elliott' 
    ] 

    # here's the neat part which saves you from iterating over the `li` elements 
    actual_books = books.all_inner_texts() 

    assert actual_books == expected_books