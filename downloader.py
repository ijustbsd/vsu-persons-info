# -*- coding: utf-8 -*-

import json
import requests

with open('persons.json', encoding='utf-8') as outfile:
    persons = json.load(outfile)

for index, person in enumerate(persons):
    filename = person['photo_url'].split('=')[1]
    path = 'photos/{}.jpg'.format(filename)
    with open(path, 'wb') as infile:
        request = requests.get(person['photo_url'])
        infile.write(request.content)
    length = len(persons)
    print('{} из {}'.format(index + 1, length))
