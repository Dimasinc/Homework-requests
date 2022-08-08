import requests

# Задача № 1:
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

# intelligence_hero()
# Hulk id = 332
# CA id = 149
# Thanos id = 655


# Задача № 2:
Token = ' '
class YandexDisk:
    def __init__(self, token):
        self.token = Token

    def headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def upload_link(self, disk_file_path):
        url = "http://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_disk(self, disk_file_path, filename):
        href = self.upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))




file_up = YandexDisk(token=Token)

# file_up.upload_disk(disk_file_path='netology/test.txt', filename='test.txt')


