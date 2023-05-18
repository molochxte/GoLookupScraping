## Run Container
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome

Selenium Grid should be accessible
http://localhost:4444/ui#/sessions 

# Run inputs.sh
- Used to run multiple inputs and outputs to log.txt

## Run Scraper.Py 
- Look at video feed in localhost. (Default password is 'Secret')
- Scraper.Py has 1 TestSuite with 2 primary functions
    - def testFormVisibility(self):
    - def testFormSubmission(self):
- main()
    - Verifies input
    - Holds XPATH variables 

# Run Webpage_Processor.Py
- Webpage_processor.py requires an existing webpage.html file to run
- If the page is the "No Results" page, it will print
- If the page has results, it will print:
    - The number of results
    - The numbers of results in each category
    - The results in the tableview for each "person" found with the input

---
# DevLog // Notes

## Selenium: Finding Form Elements
Had trouble finding xPath.. used an extension to locate it. 
The downside of using an exact path like this is it will run into an error if the webpage structure ever changes.
https://addons.mozilla.org/en-US/firefox/addon/xpath_finder/

## UnitTests
I decided to use unittests:
- to make it easier to fix errors
- don't need to open selenium view to see progress
- UnitTests have poor coverage: 
    - Checks for form visiblity
    - Submits form

## Next Up:
- Need to make errors / output more clear for logging purposes
- Console output is unclear // only used for debugging

## Issues
- web_processor.py prints out Education Records twice
