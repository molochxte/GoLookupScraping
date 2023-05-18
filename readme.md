## Run Container
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome

Selenium Grid should be accessible
http://localhost:4444/ui#/sessions 

## Run Scraper.Py 
Look at video feed in localhost. (Default password is 'Secret')

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

## inputs.sh
Used to run multiple inputs and outputs to log.txt

## Next Up:
- Need to make errors / output more clear for logging purposes

## Issues
- web_processor.py prints out Education Records twice

