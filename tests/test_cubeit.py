from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

def test_cubeit(page: Page):
    page.goto(BASE_URL)
    input = page.get_by_placeholder("Enter cube number:")
    input.fill("10")

    page.get_by_role("button", name="Convert").click()

    result = page.locator("css=div#result")
    expect(result).to_have_text("The cube is: 1000")

def test_cubeit_empty_input(page: Page):
    page.goto(BASE_URL)
    input = page.get_by_placeholder("Enter cube number:")
    input.fill("")

    page.get_by_role("button", name="Convert").click()

    result = page.locator("css=div#result")
    expect(result).to_have_text("Please enter a number.")