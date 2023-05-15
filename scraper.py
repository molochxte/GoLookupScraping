from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# XPATH to elements on webpage 
form_XPATH = "//*[@id=\"topfrm\"]"
firstName_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/input[3]"
lastName_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/input[4]"
location_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/select" # location is a dropdown
submit_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/button"

# Inputs to test
firstName_input = ""
lastName_input = ""    
location_input = ""

class GoLookupSearch(unittest.TestCase): 
    def setUp(self):
        print("Test Execution Started")
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options   
        )
        self.driver.get("https://golookup.com/")

    # FORM
    def testFormVisibility(self):
        driver = self.driver
        form = driver.find_element(By.XPATH, form_XPATH)
        self.assertTrue(form.is_displayed(), "Form element not found")

    # FIRST NAME
    def testFirstNameVisibility(self):
        firstName_Form = self.driver.find_element(By.XPATH, firstName_XPATH)
        self.assertTrue(firstName_Form.is_displayed(), "First Name element not found")

    def testEnterFirstName(self):
        firstName_Form = self.driver.find_element(By.XPATH, firstName_XPATH)
        firstName_Form.send_keys("Jane")
        self.assertEqual(firstName_Form.get_attribute("value"), lastName_input, "Incorrect First Name entered")

    # LAST NAME
    def testLastNameVisibility(self):
        firstName_Form = self.driver.find_element(By.XPATH, lastName_XPATH)
        self.assertTrue(firstName_Form.is_displayed(), "Last Name element not found")

    def testEnterLastName(self):
        firstName_Form = self.driver.find_element(By.XPATH, lastName_XPATH)
        firstName_Form.send_keys(lastName_input)
        self.assertEqual(firstName_Form.get_attribute(lastName_input), lastName_input, "Incorrect Last Name entered")

    # LOCATION
    def testLocationVisibility(self):
        location_Form = self.driver.find_element(By.XPATH, location_XPATH)
        self.assertTrue(location_Form.is_displayed(), "Location element not found")

    def testEnterLocation(self):
        location_Form = self.driver.find_element(By.XPATH, location_XPATH)
        location_Form.click()
        option = f'//option[text()="{location_input}"]'
        location_option = self.driver.find_element(By.XPATH, option)
        self.assertEqual(location_option.get_attribute(location_input))
        
    def testSumbission(self):
        submit_Form = self.driver.find_element(By.XPATH, submit_XPATH)
        submit_Form.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
