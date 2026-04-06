import pytest
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # Navigate to the login page
    page.goto("https://www.saucedemo.com/")

    # Fill in valid username
    page.fill("#user-name", "standard_user")

    # Fill in valid password
    page.fill("#password", "secret_sauce")

    # Click the login button
    page.click("#login-button")

    # Assert that the user is redirected to the inventory page
    # Option 1: Assert the URL
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Option 2: Assert an element specific to the inventory page is visible
    expect(page.locator(".title")).to_have_text("Products")
    expect(page.locator(".shopping_cart_link")).to_be_visible()