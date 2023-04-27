from bs4 import BeautifulSoup
import requests
import pandas as pd

def parse1():
    page = requests.get('https://omsk.hh.ru/search/vacancy?text=python&area=68', headers={'User-Agent': 'Custom'})
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', class_='serp-item')  # находим  контейнер с нужным классом
    df = pd.DataFrame(columns=['vacancy','salary'])

    for data in block:  # проходим циклом по содержимому контейнера
            name = data.find('a', class_='serp-item__title')
            salary = data.find('span', {'class': 'bloko-header-section-3'})
            if (salary != None):
                description = {'vacancy':name.text,'salary':salary.text}
            else:
                description = {'vacancy': name.text, 'salary': 'Не указана'}
            df = pd.concat([df, pd.DataFrame([description])], ignore_index=True)
    df.index += 1
    df.to_excel('vacancy.xlsx')
    print(df)
