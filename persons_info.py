# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.vsu.ru/ru/persons/?dep=80000000000186DA')

soup = BeautifulSoup(page.text, 'html.parser')

persons_list = soup.find_all(class_='person-item')

result = []

for person in persons_list:
    photo = person.find(class_='person-foto')
    photo_url = 'https://www.vsu.ru/ru/persons/' + photo.find('a')['href']

    fio = person.find(class_='person-fio')
    fio_text = fio.find('span').contents[0]
    name, surname, patronymic = fio_text.split()

    details = person.find_all(class_='details')
    details_list = [detail.contents[0].split('| ')[1] for detail in details]

    person_dict = {
        'photo_url': photo_url,
        'name': name,
        'surname': surname,
        'patronymic': patronymic,
        'details': details_list
    }

    result.append(person_dict)

with open('persons.json', 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=2)
