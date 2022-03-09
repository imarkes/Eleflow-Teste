import csv
from typing import Set, Any

import requests
from data_engineer_test.vra import FilesVRA


class AerodromosCSV:

    def __init__(self):
        self.response = []
        self.result_VRA = FilesVRA()
        self.list_data_VRA = list(self.result_VRA.read_all_files_in_path())

    def get_codgos_icao(self):
        cods_icao_origem = [cod['icaoaeródromo_origem'] for cod in self.list_data_VRA]
        cods_icao_destino = [cod['icaoaeródromo_destino'] for cod in self.list_data_VRA]
        codgos = set(cods_icao_origem + cods_icao_destino)
        return codgos

    def response_get_url(self):
        url = "https://airport-info.p.rapidapi.com/airport"

        headers = {
            'x-rapidapi-host': "airport-info.p.rapidapi.com",
            'x-rapidapi-key': "4e66b5eee7mshe07cecc516f5f82p1d7870jsnece9b9399d9e"
        }

        for cod in self.get_codgos_icao():
            print('CODGOS->:',cod)
            querystring = {"icao": cod}
            self.response = [{'id': 633, 'iata': 'BEL', 'icao': 'SBBE', 'name': 'Val de Cans International Airport',
                         'location': 'Belém, Pará, Brazil', 'street_number': 's/n', 'street': 'Avenida Júlio César',
                         'city': '',
                         'county': 'Belém', 'state': 'Pará', 'country_iso': 'BR', 'country': 'Brazil',
                         'postal_code': '66115-970', 'phone': '+55 91 3210-6000', 'latitude': -1.3820615,
                         'longitude': -48.477524, 'uct': -180,
                         'website': 'http://www4.infraero.gov.br/aeroportos/aeroporto-internacional-de-belem-val-de-cans-julio-cezar-ribeiro/'},
                        {'id': 7941, 'iata': 'VCP', 'icao': 'SBKP', 'name': 'Viracopos/Campinas International Airport',
                         'location': 'São Paulo / Campinas, São Paulo, Brazil', 'street_number': 'km 66',
                         'street': 'Rodovia Santos Dumont',
                         'city': '', 'county': 'Campinas', 'state': 'São Paulo', 'country_iso': 'BR',
                         'country': 'Brazil',
                         'postal_code': '13055-900', 'phone': '+55 19 3725-5000', 'latitude': -23.008205,
                         'longitude': -47.13757,
                         'uct': -180, 'website': 'http://www.viracopos.com/'},
                        ]
            #resp = requests.request("GET", url, headers=headers, params=querystring).json()
            #self.response.append(resp)
            #return self.response

    def generate_csv(self):
        with open('aerodromos.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = list(self.response[0].keys())

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in range(len(self.response)):
                print(self.response[row]['id'])
                # print(list(response[0].values()))
                # writer.writerow({list(response[0].keys()): list(response[0].values())})

                writer.writerow(
                    {'id': self.response[row]['id'], 'iata': self.response[row]['iata'], 'icao': self.response[row]['icao'],
                     'name': self.response[row]['name'],
                     'location': self.response[row]['location'], 'street_number': self.response[row]['street_number'],
                     'street': self.response[row]['street'],
                     'city': self.response[row]['city'], 'county': self.response[row]['county'], 'state': self.response[row]['state'],
                     'country_iso': self.response[row]['country_iso'],
                     'country': self.response[row]['country'], 'postal_code': self.response[row]['postal_code'],
                     'phone': self.response[row]['phone'],
                     'latitude': self.response[row]['latitude'],
                     'longitude': self.response[row]['longitude'], 'uct': self.response[row]['uct'],
                     'website': self.response[row]['website']}
                )


if __name__ == '__main__':
    a = AerodromosCSV()
    a.response_get_url()
    a.generate_csv()

# ['id', 'iata', 'icao', 'name', 'location', 'street_number', 'street', 'city', 'county', 'state', 'country_iso',
#  'country', 'postal_code', 'phone', 'latitude', 'longitude', 'uct', 'website']
