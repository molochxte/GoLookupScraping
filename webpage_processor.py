from bs4 import BeautifulSoup

with open('webpage.html') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

def getNumberOfResults():
    div_element = soup.find('h1', class_="text-white text-left-mobile text-center mt-0 mb-0 title-padding")
    strong_element = div_element.find('strong')
    return strong_element.text

def getResultCategoryCount():
    ul_element = soup.find('ul', class_="list-unstyled fs-18 text-white mb-0")
    for li_elements in ul_element.find_all('li'):
        categoryCount = ' '.join(li_elements.stripped_strings)
        print(categoryCount)
    return categoryCount

def getResultsTable():
    div_elements = soup.find_all('div', class_='tr clearfix process-record mobile-margin-5')
    persons_dict = {}
    for div_element in div_elements:
        # Extract data from the data-* attributes
        first_name = div_element.get('data-firstname')
        last_name = div_element.get('data-lastname')
        age = div_element.get('data-age')
        location = div_element.get('data-location')
        person_enc = div_element.get('data-person-enc')
        persons_dict[person_enc] = [first_name, last_name, age, location]
        
        # Print the extracted data
        # print("========================")
        # print("First Name:", first_name)
        # print("Last Name:", last_name)
        # print("Age:", age)
        # print("Location:", location)
        # #print("Person Enc:", person_enc)

    return persons_dict

        

if __name__ == "__main__":
    print(getNumberOfResults())
    print("========================")
    print(getResultCategoryCount())
    print("========================")
    results_table = getResultsTable()

    for person_id, info in results_table.items():
        print(info)