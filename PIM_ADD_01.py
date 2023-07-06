import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MyPIMTestCase1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        print("setup called")

    def tearDown(self):
        print("Tear down called")
        self.driver.quit()

    def test_PIMAddTC1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(5)

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        time.sleep(5)
        # Navigate to the Add Employee page
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(5)
        #add person
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()

        time.sleep(5)
        # Fill in the employee details
        first_name = self.driver.find_element(By.NAME, "firstName")
        last_name = self.driver.find_element(By.NAME, "lastName")
        middle_name = self.driver.find_element(By.NAME, "middleName")
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        middle_name.send_keys("Ji")


        #click save
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()

        time.sleep(13)

        personal_details = self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6")

        self.assertEqual(True, personal_details.is_displayed())

        nick_name = self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input")

        nick_name.send_keys("NIck_name")

        self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        time.sleep(10)



        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        self.assertEqual(True, username.is_displayed())

        self.driver.close()


if __name__ == '__main__':
    unittest.main()
