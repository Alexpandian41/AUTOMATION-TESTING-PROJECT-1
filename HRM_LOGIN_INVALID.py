import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MyLoginTestCase2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        print("setup called")

    def tearDown(self):
        print("Tear down called")
        self.driver.quit()

    def test_testLoginTC1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(5)

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("invalid password")
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)

        dashboard = self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")

        self.assertEqual(True,dashboard.is_displayed())



if __name__ == '__main__':
    unittest.main()
