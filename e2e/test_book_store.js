const { test, expect } = require('@playwright/test');
test('should show the books list', async ({ page }) => {

    //Once we've navigated to the page that the form is on
    page.goto("https//localhost:5001/books")

    //We need to grab and fill the first field. Let's start with "Title".
    //There are a few ways to do this but I'm going to use get_by_placeholder
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    //Now "Author"
    page.get_by_placeholder("Author").fill("Geronimo")

    //OK so we know how to fill in the two fields. 
    //How about pressing the button?
    page.get_by_role("button", name="Submit").click()

    });