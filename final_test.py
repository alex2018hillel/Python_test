import unittest
import configparser
from utils.login_page import Login_page
from utils.create_page import Create_mail
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)

    def test_first(self, id = "ID_109"):
        wdriver = self.driver
        parser = configparser.ConfigParser()
        parser.read('simple_config.ini')
        url = parser.get('data', 'url')
        user_name = parser.get('data', 'username')
        password = parser.get('data', 'password')

        # Login to mailbox form
        wdriver.get(url)
        login_field = wdriver.find_element_by_xpath(Login_page.login_field)
        login_field.send_keys(user_name)
        password_field = wdriver.find_element_by_xpath(Login_page.password_field)
        password_field.send_keys(password)
        button_login = wdriver.find_element_by_xpath(Login_page.button_login)
        button_login.click()
        wdriver.implicitly_wait(10)
        user_mail = wdriver.find_element_by_xpath(Login_page.user_mail)
        print(user_mail.text)
        assert user_mail.text == Create_mail.expected_name

        # Create e-mail
        wdriver.find_element_by_xpath(Create_mail.create_button).click()
        wdriver.find_element_by_xpath(Create_mail.fild_input).send_keys(Create_mail.expected_name)
        wdriver.find_element_by_xpath(Create_mail.fild_subject).send_keys(id)
        wdriver.find_element_by_xpath(Create_mail.submit_button).click()
        wdriver.find_element_by_xpath("//a[@id='0']/span[4]").click()
        wdriver.implicitly_wait(10)

        # Find e-mail
        elem = wdriver.find_elements_by_xpath("//*[text()='ID_109']")[0]
        print(elem.text)
        assert elem.text == id

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()