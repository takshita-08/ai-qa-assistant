import pytest
from pages.login_page import LoginPage
from config import INVALID_PASSWORD, INVALID_USER, VALID_PASSWORD, VALID_USER


@pytest.mark.parametrize("username, password", [
    ("standard_user", "standard_user"), 
    ("secret_sauce", "secret_sauce"),
    ("performance_glitch_user", "invalid"),
    ("visual_user", "incorrrect"),
    ("incorrect", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    (INVALID_USER,INVALID_PASSWORD),
    ("", "")
    ])
def test_invalid_login(page, username, password):
    login_page = LoginPage(page)
    login_page.load_page()
    login_page.login(username,password)
    
    error=login_page.get_error_msg()
    # Assertion
    assert "inventory" not in page.url
    assert error.is_visible()
    assert "Username and password do not match" or "Sorry, this user has been locked out" in error.inner_text()

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"), 
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    (VALID_USER,VALID_PASSWORD)
    ])
def test_login_valid(page, username, password):
    login_page = LoginPage(page)
    login_page.load_page()
    login_page.login(username,password)

    error = login_page.page.locator("[data-test='error']")
    if error.is_visible():
     print("Error:", error.inner_text())
    
    assert "inventory" in page.url
    assert  login_page.get_title() == "Products"


