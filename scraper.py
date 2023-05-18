from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import sys
from locations import locations 
import re #verify valid input with regex

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
            submitCity_Form = self.driver.find_element(By.XPATH, submitCityOption_XPATH)
            submitCity_Form.click()

        time.sleep(30)

        # VIEW RESULTS
        try:
            found_results = self.driver.find_element(By.XPATH, results_XPATH) 
            print(found_results.text)
        except:
            # no records found
            result_message = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div/div")
            print(result_message.text) 
        
        # save webpage regardless
        webpage = self.driver.page_source
        with open("webpage.html", "w", encoding="utf-8") as file:
            file.write(webpage)

        time.sleep(10)
    def tearDown(self):
        self.driver.quit()

def test_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GoLookupSearch))
    return suite

if __name__ == "__main__":
    
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print(sys.argv[1:])
        print("Expected: python scraper.py <first_name> <last_name> <US State> <City>(Optional)")
        sys.exit(1)
    
    for arg in sys.argv[1:]:
        if re.search(r'\d|\W', arg):
           
            print("Special characters and numbers are not accepted.")
            sys.exit(1)

    if sys.argv[3] not in locations:
        print("Recieved:", sys.argv[1:])
        print("Expected: python scraper.py <first_name> <last_name> <US State> <City>(Optional)")
        print(sys.argv[4], "is not a state")
        sys.exit(1)

    if len(sys.argv) == 5: 
        city_input = sys.argv[4]
    else:
        city_input = ""

    # Inputs to test
    firstName_input = sys.argv[1]
    lastName_input = sys.argv[2] 
    location_input = locations.index(sys.argv[3].title())

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

    suite = test_suit()
    runner = unittest.TextTestRunner()
    runner.run(suite)
