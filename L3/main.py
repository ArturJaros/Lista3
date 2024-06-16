import requests

BASE_API_URL = 'https://swapi.dev/api/'
person_id_list = [1, 2, 3000]

for id in person_id_list:
    res = requests.get(f'{BASE_API_URL}people/{id}/')
    if res.status_code == 200:
        data = res.json()
        print(data.keys())
        print("Check: PASSED")
    else:
        print("Check: FAILED")
