import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MyPIMTestCase3(unittest.TestCase):

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
        # Navigate to the pim page
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(5)
        #edit person
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]").click()
        time.sleep(5)
        #confirm to delete
        confirm_delete = self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[3]/div/div/div/div[3]/button[2]")

        self.assertEqual(True, confirm_delete.is_displayed())

        confirm_delete.click()

        time.sleep(5)




        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        self.assertEqual(True, username.is_displayed())

        self.driver.close()


if __name__ == '__main__':
    unittest.main()
