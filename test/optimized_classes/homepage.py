from selenium.webdriver.common.by import By
class homepage:
    def __init__(self, driver):
        self.driver = driver
        
    shop = (By.XPATH,"//a[text()='Shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radiobtn = (By.CSS_SELECTOR, "#inlineRadio1")
    gender = (By.ID,"exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR,".btn.btn-success")
    alert = (By.CLASS_NAME, "alert-success")


    def shopitems(self):
        return self.driver.find_element(*homepage.shop)
    def getname(self):
        return self.driver.find_element(*homepage.name)
    def getemail(self):
        return self.driver.find_element(*homepage.email)
    def getpassword(self):
        return self.driver.find_element(*homepage.password)
    def getcheckbox(self):
        return self.driver.find_element(*homepage.checkbox)
    def getradiobtn(self):
        return self.driver.find_element(*homepage.radiobtn)
    def getgender(self):
        return self.driver.find_element(*homepage.gender)
    def submitform(self):
        return self.driver.find_element(*homepage.submit)
    def alertmessage(self):
        return self.driver.find_element(*homepage.alert)

