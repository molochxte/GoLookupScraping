from bs4 import BeautifulSoup

with open('webpage.html') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

def getNumberOfResults():
    div_element = soup.find('h1', class_="text-white text-left-mobile text-center mt-0 mb-0 title-padding")
    strong_element = div_element.find('strong')
    print(strong_element.text)

def getResultCategoryCount():
    pass

def getResultsTable():
    pass

if __name__ == "__main__":
    getNumberOfResults()