import requests
from bs4 import BeautifulSoup


# def go_to_next_page(current_url):
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
indeed_result = requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50',headers=headers)
soup = BeautifulSoup(indeed_result.text,'html.parser')
pagination = soup.find('ul',{'class':'pagination-list'})
links = pagination.find_all('li')
for link in links[-1]:
    next_page=link['href']
print(next_page)
    # print(link.find('a'))
    # return (current_url+next_page)


#     for page in next:
#         print(page['href'])
# # print(next[-1])

# def go_to_next_page(current_url):
#     headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
#     indeed_result = requests.get(current_url,headers=headers)
#     soup = BeautifulSoup(indeed_result.text,'html.parser')
#     pagination = soup.find('ul',{'class':'pagination-list'})
#     links = pagination.find_all('li')
#     for link in links[-1]:
#         next_page=link['href']
#         while
#     return (current_url+next_page)


