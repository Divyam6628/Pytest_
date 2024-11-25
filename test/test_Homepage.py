import pytest
from baseclass import Baseclass
from optimized_classes.homepage import homepage

class TestHomepage(Baseclass):

    def test_form_submission(self):
        Home = homepage(self.driver)
        Home.getname().send_keys("Rahul")
        Home.getemail().send_keys("hello@gmail.com")
        Home.getpassword().send_keys("123456")
        Home.getcheckbox().click()
        Home.getradiobtn().click()
        self.selectfromdropdown(Home.getgender(), "Male")

        Home.submitform().click()
        message = Home.alertmessage().text
        print(message)
        assert "Success" in message

    # @pytest.fixture(params=[a,b,c])
    # def getdata(self, request)
    #     return request.param
