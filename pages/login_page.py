from config import BASE_URL

class LoginPage:
    def __init__(self, page) -> None:
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.loginbtn = "#login-button"
        self.error = "[data-test='error']"
        self.title = ".title"

    def load_page(self):
        self.page.goto(BASE_URL)

    
    def login(self,username,password):
        # Enter credentials
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        
        # Click login
        self.page.click(self.loginbtn)
     

    def get_error_msg(self):
        return self.page.locator(self.error)
    
    def get_title(self):
        return  self.page.locator(self.title).inner_text()

        

