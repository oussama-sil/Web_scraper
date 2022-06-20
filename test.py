
import requests
from bs4 import BeautifulSoup


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key+":"+a_dict[key],end="\n"*2)

arr = []
arr.append(a_dict)
for el in arr:
    print(a_dict)


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results =   soup.find(id="ResultsContainer")

#print(results.prettify()) #? to print html code 

#getting the list 
job_elements = results.find_all("div", class_="card-content")
# print(job_elements[0]) #? it s a list 

for job_element in job_elements:
    # print(job_element, end="\n"*2)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()