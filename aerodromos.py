import csv
import requests
from data_engineer_test.vra import FilesVRA


class AerodromosCSV:
    """Generate File CSV Aerodromo with base in all codgos ICAO."""

    def __init__(self):
        self.codgos = None
        self.response = []
        self.result_VRA = FilesVRA()
        self.list_data_VRA = list(self.result_VRA.read_all_files_in_path())

    def get_codgos_icao(self):
        """Return codgos ICAO to file VRA."""
        cods_icao_origem = [cod['icaoaeródromo_origem'] for cod in self.list_data_VRA]
        cods_icao_destino = [cod['icaoaeródromo_destino'] for cod in self.list_data_VRA]
        self.codgos = set(cods_icao_origem + cods_icao_destino)
        return self.codgos

    def response_get_url(self):
        """Get data URL."""
        url = "https://airport-info.p.rapidapi.com/airport"
        headers = {
            'x-rapidapi-host': "airport-info.p.rapidapi.com",
            'x-rapidapi-key': "4e66b5eee7mshe07cecc516f5f82p1d7870jsnece9b9399d9e"
        }

        for cod in self.codgos:
            querystring = {"icao": cod}
            resp = requests.request("GET", url, headers=headers, params=querystring).json()
            self.response.append(resp)

    def generate_csv(self):
        """Generate CSV File."""
        with open('aerodromos.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = list(self.response[0].keys())

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in range(len(self.response)):

                writer.writerow(
                    {'id': self.response[row]['id'], 'iata': self.response[row]['iata'],
                     'icao': self.response[row]['icao'],'name': self.response[row]['name'],
                     'location': self.response[row]['location'], 'street_number': self.response[row]['street_number'],
                     'street': self.response[row]['street'],'city': self.response[row]['city'],
                     'county': self.response[row]['county'],'state': self.response[row]['state'],
                     'country_iso': self.response[row]['country_iso'],'country': self.response[row]['country'],
                     'postal_code': self.response[row]['postal_code'],'phone': self.response[row]['phone'],
                     'latitude': self.response[row]['latitude'],'longitude': self.response[row]['longitude'],
                     'uct': self.response[row]['uct'],'website': self.response[row]['website']}
                )


if __name__ == '__main__':
    a = AerodromosCSV()
    a.get_codgos_icao()
    a.response_get_url()
    a.generate_csv()
