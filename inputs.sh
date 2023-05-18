#!/bin/bash

# expecting: 7 results
python3 scraper.py Jane Doe Alabama && python3 webpage_processor.py >> log.txt

# expecting: 0 results 
python3 scraper.py Jay Quedado Washington && python3 webpage_processor.py >> log.txt

# expecting: 1 results (with City option)
python3 scraper.py Jay Quedado Idaho Boise && python3 webpage_processor.py >> log.txt

# expecting: error due to invalid input (numbers or special characters)
python3 scraper.py Jane-=-= Doe Alabama && python3 webpage_processor.py >> log.txt
python3 scraper.py Jane Doe22 Alabama && python3 webpage_processor.py >> log.txt

# expecting: error due to incorrect number of args
python3 scraper.py Jane Doe && python3 webpage_processor.py >> log.txt
python3 scraper.py Jane Doe Alabama Boise Hello && python3 webpage_processor.py >> log.txt


