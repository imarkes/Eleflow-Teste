import csv
import requests
from data_engineer_test.vra import FilesVRA


result_VRA = FilesVRA()
list_data_VRA = list(result_VRA.read_all_files_in_path())

cods_icao_origem = [cod['icaoaeródromo_origem'] for cod in list_data_VRA]
cods_icao_destino = [cod['icaoaeródromo_destino'] for cod in list_data_VRA]



url = "https://airport-info.p.rapidapi.com/airport"

querystring = {"icao": "SBKP"}

headers = {
    'x-rapidapi-host': "airport-info.p.rapidapi.com",
    'x-rapidapi-key': "4e66b5eee7mshe07cecc516f5f82p1d7870jsnece9b9399d9e"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

with open('aerodromos.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = list(response)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow(response)

