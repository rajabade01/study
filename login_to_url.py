from config.driver_initialization import WebDriverConnection
'''This class will get web driver session and login to the site provided '''

class Login():

    '''This method will get the appropriate diver session'''
    def get_web_driver(self,driver_type):
        driver = WebDriverConnection()
        if(driver_type == "Chrome"):
            return driver.getChromeDriver()
        else:
            return driver.getFFDriver()
    '''this method will take params as diver session and site to login and do the site login'''
    def site_login(self,driver, site):
        driver.get(site)
        driver.find_element_by_id("ID").send_keys("Username")
        driver.find_element_by_id("ID").send_keys("Password")
        driver.find_element_by_id("ID").send_keys("Sign in").click()

    '''this method will get all the repos from the github'''
    def get_repos(self, driver,):
        driver.get("https://github.com/")
        driver.find_element_by_id("ID").send_keys("Repositories").click()


if __name__ == "__main__":
    username = ""
    password = ""
    site = "https://github.com/login"
    login = Login()
    driver = login.get_web_driver("Chrome")
    login.site_login(driver, username, password)

