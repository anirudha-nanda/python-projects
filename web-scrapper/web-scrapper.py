import requests
import pprint
from bs4 import BeautifulSoup
"""
Gets code from the link below and then stores the data returned back from the server in a python object.

"""
URL = 'https://www.monster.ca/jobs/search/?q=Machine-Learning'
page = requests.get(URL)

#pretty printing the html contents. 
#pp = pprint.PrettyPrinter()

#pp.pprint(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
#print(results.prettify())

#got an iterable contains all jobs
job_elems = results.find_all('section', class_='card-content')
#print(job_elems.prettify())

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.strip())
    print()        


