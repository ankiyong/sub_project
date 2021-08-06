import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}'
def extrat_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,'html.parser')
    pagination = soup.find('ul',{'class':'pagination-list'})
    links = pagination.find_all('li')
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.text))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    comapny = html.find('span', {'class': 'companyName'}).string
    if comapny is not None:
        pass
    else:
        comapny = None
    titles = html.find_all('span')
    title = titles[0].string
    if titles[0].string == 'new':
        title = titles[1].string
    else:
        pass
    location = html.find('div',{'class':'companyLocation'}).string
    return {'title':title,'company':comapny,'location':location}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page+1):
        print(f'Scrapping page {page}')
        result = requests.get(f'{URL}&start={page * LIMIT}')
        # print(f'{URL}start={page * LIMIT}')
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all('table',{'class':'jobCard_mainContent'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs






