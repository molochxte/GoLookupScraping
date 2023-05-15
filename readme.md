## Run Container
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome

Selenium Grid should be accessible
http://localhost:4444/ui#/sessions 

## Run Scraper.Py 
Look at video feed in localhost. (Default password is 'Secret')

---

## Entering First Name // Last Name into Form
Had trouble finding xPath.. used an extension to locate it. 
The downside of using an exact path like this is it will run into an error if the webpage structure ever changes.
https://addons.mozilla.org/en-US/firefox/addon/xpath_finder/

