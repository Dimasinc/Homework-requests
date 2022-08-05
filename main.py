import requests

def intelligence_hero():
    id = input("Введите через запятую id героев для сравнения:").replace(' ', '')
    list_id = id.split(',')
    intelligence_hero = {"name": " ", "intelligence": "0"}
    for var in list_id:
        url = f"https://akabab.github.io/superhero-api/api/id/{var}.json"
        hero = requests.get(url)
        for var in hero.json():
            if var == 'powerstats':
                for var_1 in hero.json()['powerstats']:
                    if var_1 == 'intelligence':
                        powerstats_dict = hero.json()['powerstats']
                        if int(powerstats_dict["intelligence"]) > int(intelligence_hero["intelligence"]):
                            intelligence_hero.update({'name': hero.json()['name'], 'intelligence': powerstats_dict['intelligence']})
    print(f"Герой с самым высоким интеллектом:{intelligence_hero['name']}, уровень интеллекта: {intelligence_hero['intelligence']}")

intelligence_hero()


# Hulk id = 332
# CA id = 149
# Thanos id = 655
