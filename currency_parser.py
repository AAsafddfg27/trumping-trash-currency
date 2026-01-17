import requests
from bs4 import BeautifulSoup

headers = {'Accept': 'text/html', 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}

URL = 'https://cbr.ru'

response = requests.get(URL, headers=headers)

if response.status_code != 200:
    print(f'Error: {response.status_code}')
    print(response.text[:500])
else:
    print('OK')

html = response.text

soup = BeautifulSoup(html, 'lxml')

currency_status = soup.find_all('div', class_='main-indicator_rate')


for rate in currency_status:
    rates = rate.find_all('div', class_='col-md-2')
    currency = rates[0].get_text(strip=True)
    today = rates[2].get_text(strip=True)
    yestarday= rates[1].get_text(strip=True)
    print(f'{currency}: {today} (вчера {yestarday})')