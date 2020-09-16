import requests


def to_find_intelligence(name):
    address = 'https://superheroapi.com/api/2619421814940190/search/' + name
    response = requests.get(address)
    response = response.json()
    intelligence = int(response['results'][0]['powerstats']['intelligence'])
    return intelligence


heroes = ['Hulk', 'Captain_America', 'Thanos']
max_intelligence = 0
name_intelligence = 'Unknown'
for hero in heroes:
    current_intelligence = to_find_intelligence(hero)
    if current_intelligence > max_intelligence:
        max_intelligence = current_intelligence
        name_intelligence = hero
print(f'Самый умный супергерой {name_intelligence}.')
