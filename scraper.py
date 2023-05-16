from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import sys

# Location Options 
locations = [
    '', 
    'All States',
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'District of Columbia',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming'
]


# Inputs to test
firstName_input = "Jane"
lastName_input = "Doe" 
location_input = locations.index("Alaska")
city_input = "" #OPTIONAL 

# XPATH to elements on webpage
# Placed here for easier editing
form_XPATH = "//*[@id=\"topfrm\"]"
firstName_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/input[3]"
lastName_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/input[4]"
locationOption_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/select/option[" + str(location_input) + "]"
submit_XPATH = "/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/button"

cityOption_XPATH = "/html/body/div[1]/div[1]/section/div[2]/div/div/div/form/div[2]/input"
submitCityOption_XPATH = "/html/body/div[1]/div[1]/section/div[2]/div/div/div/form/div[3]/button[1]"

results_XPATH = "/html/body/div[1]/div[1]/section/div/section/div[1]/div[2]/div/div[1]/h1"


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

    def testFormVisibility(self):
        driver = self.driver
        form = driver.find_element(By.XPATH, form_XPATH)
        self.assertTrue(form.is_displayed(), "Form element not found")
        
        firstName_Form = self.driver.find_element(By.XPATH, firstName_XPATH)
        self.assertTrue(firstName_Form.is_displayed(), "First Name element not found")

        firstName_Form = self.driver.find_element(By.XPATH, lastName_XPATH)
        self.assertTrue(firstName_Form.is_displayed(), "Last Name element not found")

        location_Form = self.driver.find_element(By.XPATH, locationOption_XPATH)
        self.assertTrue(location_Form.is_displayed(), "Location element not found")

    def testFormSubmission(self):
        # NAME
        firstName_Form = self.driver.find_element(By.XPATH, firstName_XPATH)
        firstName_Form.send_keys(firstName_input)
        self.assertEqual(firstName_Form.get_attribute("value"), firstName_input, "Incorrect First Name entered")
        
        lastName_Form = self.driver.find_element(By.XPATH, lastName_XPATH)
        lastName_Form.send_keys(lastName_input)
        self.assertEqual(lastName_Form.get_attribute("value"), lastName_input, "Incorrect Last Name entered")

        # LOCATION 
        location_option = self.driver.find_element(By.XPATH, locationOption_XPATH)
        selected_option_text = location_option.text
        location_option.click()
        self.assertEqual(selected_option_text, locations[location_input], "Incorrect location selected")

        # SUBMIT FORM
        submit_Form = self.driver.find_element(By.XPATH, submit_XPATH)
        submit_Form.click()

        # CITY IS OPTIONAL
        time.sleep(10)
        if city_input != "":
            city_Form = self.driver.find_element(By.XPATH,cityOption_XPATH)
            city_Form.send_keys(city_input)
            submitCity_Form = self.driver.find_element(By.XPATH)
            submitCity_Form.click()

        time.sleep(30)

        # VIEW RESULTS
        results = self.driver.find_element(By.XPATH, results_XPATH)        
        results_text = results.text
        print(results_text)

        time.sleep(10)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
