import requests
from bs4 import BeautifulSoup
import time

url = requests.get('https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Nairobi%2C%20Kenya&geoId=101339379&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
soup = BeautifulSoup(url, 'lxml')
jobs = soup.find('ul', class_='jobs-search__results-list')
lists = jobs.findAll('li')


def find_job():
    for listing in lists:
        role = listing.find('h3', class_='base-search-card__title').text.replace(' ', '')
        company_name = listing.find('h4', class_='base-search-card__subtitle').text.replace(' ', '')
        link = listing.div.a['href']
        with open('post', 'w') as f:
            f.write(f'Company name : {company_name.strip()} \n')
            f.write(f'Role : {role.strip()} \n')
            f.write(f'Link : {link}')


if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} seconds ..')
        time.sleep(time_wait * 10)
