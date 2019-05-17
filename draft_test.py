import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class LoginMailBox(unittest.TestCase):

    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)

    def test_mail_box(self, id = "ID_107"):
        #Login to mailbox form
        wdriver = self.driver
        self.driver.get("https://mail.ukr.net/desktop/login")
        login_field = self.driver.find_element_by_xpath("//*[@id='id-l']")
        login_field.send_keys("alex2019hillel")
        password_field = self.driver.find_element_by_xpath("//*[@id='id-p']")
        password_field.send_keys("A661956a")
        button_login = self.driver.find_element_by_xpath("//*[@type='submit']")
        button_login.click()
        self.driver.implicitly_wait(10)
        user_mail = self.driver.find_element_by_xpath("//*[@class='login-button__user']")
        print(user_mail.text)
        assert user_mail.text == "alex2019hillel@ukr.net"

        #Create e-mail
        self.driver.find_element_by_xpath("//div[@id='content']/aside/button").click()
        self.driver.find_element_by_xpath("//input[@name='toFieldInput']").send_keys("alex2019hillel@ukr.net")
        self.driver.find_element_by_xpath("//input[@name='subject']").send_keys(id)
        self.driver.find_element_by_xpath("//div[@id='screens']/div/div/div/button").click()
        self.driver.find_element_by_xpath("//a[@id='0']/span[4]").click()
        self.driver.implicitly_wait(10)

        #Find e-mail
        elem = wdriver.find_elements_by_xpath("//*[text()='ID_107']")[0]
        print(elem.text)
        assert elem.text == id

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()