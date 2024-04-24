import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://www.emploi.ci/recherche-jobs-cote-ivoire', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

jobs = []

job_elements = soup.find_all('div', class_='job-title')

for job_element in job_elements:

    # extract the name of the job
    campany = job_element.find('a', class_='company-name').text
    # extract the description of the job
    descriptions = job_element.find('div', class_='search-description').text
    # extract the url of the job
    link = job_element.find('a', href=True)['href']

    jobs.append(
    {
        'campany': campany,
        'description': descriptions,
        'link': link,
    }
)
    
# reading  the "jobs.csv" file and creating it if not present
csv_file = open('recherche-jobs-cote-ivoire.csv', 'w', encoding='utf-8', newline='')


# initializing the writer object to insert data in the CSV file
writer = csv.writer(csv_file)


#writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['campany', 'Descriptions', 'link'])

# writing each row of the CSV
for job in jobs:
    writer.writerow(job.values())

# End of the operation
csv_file.close()



# ScraptWebsit 2 "========================================================================"

page = requests.get('https://emploi.educarriere.ci/nos-offres', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

jobs = []

job_elements = soup.find_all('div', class_='small-post')

for job_element in job_elements:

    # extract the name of the job
    campany = job_element.find('h4')
    # extract the description of the job
    descriptions = job_element.find('p', class_='entry-title')
    # extract the url of the job
    link = job_element.find('a', href=True)['href']

    jobs.append(
    {
        'campany': campany,
        'description': descriptions,
        'link': link,
    }
)
    
# reading  the "jobs.csv" file and creating it if not present
csv_file = open('educarriere.ci-nos-offres.csv', 'w', encoding='utf-8', newline='')


# initializing the writer object to insert data in the CSV file
writer = csv.writer(csv_file)


#writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['campany', 'Descriptions', 'link'])

# writing each row of the CSV
for job in jobs:
    writer.writerow(job.values())

# End of the operation
csv_file.close()


# ScraptWebsit 3 "========================================================================"

page = requests.get('https://freeci.ci/cat%C3%A9gorie/Programmation%20et%20d%C3%A9veloppement%20web', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

jobs = []

job_elements = soup.find_all('a', class_='task-listing')

for job_element in job_elements:

    # extract the name of the job
    campany = job_element.find('h3', class_='task-listing-title break-line').text
    # extract the description of the job
    descriptions = job_element.find('span', class_='unpaid').text
    # extract the url of the job
    link = job_element.find('a', class_='task-listing', href=True)

    jobs.append(
    {
        'campany': campany,
        'description': descriptions,
        'link': link,
    }
)
    
# reading  the "jobs.csv" file and creating it if not present
csv_file = open('developpement-web.csv', 'w', encoding='utf-8', newline='')


# initializing the writer object to insert data in the CSV file
writer = csv.writer(csv_file)


#writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['campany', 'Descriptions', 'link'])

# writing each row of the CSV
for job in jobs:
    writer.writerow(job.values())

# End of the operation
csv_file.close()
