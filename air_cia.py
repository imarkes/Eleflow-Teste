import csv
import glob
import os


class FilesAIRCIA:
    def __init__(self, path='AIR_CIA') -> None:
        self.new_dict = []
        self.path = path
        self.path_csv_files = glob.glob(os.path.join(path, '*.csv'))

    def normalize_readers_csv(self, filename):
        """
        :param: ['Ivan Marques', Desenvolvedor Python]
        :return: ['ivan_marques', desenvolvedor_python]
        """

        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')

            for row in reader:
                headers = list(row)
                ICAO = headers[1].split()[0].lower()
                IATA = headers[1].split()[1].lower()
                new_header = [head.replace(' ', '_').lower() for head in headers]  # converte em snak_case
                new_header[1] = ICAO
                new_header.insert(2, IATA)
                headers = new_header

                new_values = list(row.values())
                values = new_values[1].split()
                if len(values) == 0:
                    new_values[1] = None
                else:
                    new_values[1] = values[0]

                if len(values) <= 1:
                    new_values.insert(2, None)
                else:
                    new_values.insert(2, values[1])

                new = dict(zip(headers, new_values))

                self.new_dict.append(new)
                return self.new_dict

    def read_all_files_in_path(self):
        """Return generator object FilesAIRCIA."""
        print(self.new_dict)
        for files in self.path_csv_files:
            self.normalize_readers_csv(files)

    def generate_csv_air_cia(self):
        """Generate CSV File."""
        with open('air_cia.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = list(self.new_dict[0].keys())

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in self.new_dict:

                writer.writerow({
                    'razão_social': row['razão_social'], 'icao': row['icao'],
                    'iata': row['iata'], 'cnpj': row['cnpj'], 'atividades_aéreas': row['atividades_aéreas'],
                    'endereço_sede': row['endereço_sede'], 'telefone': row['telefone'], 'e-mail': row['e-mail'],
                    'decisão_operacional': row['decisão_operacional'],
                    'data_decisão_operacional': row['data_decisão_operacional'],
                    'validade_operacional': row['validade_operacional']
                })


if __name__ == '__main__':
    a = FilesAIRCIA()
    a.read_all_files_in_path()
    a.generate_csv_air_cia()

# 'razão_social':, 'icao':, 'iata':, 'cnpj':, 'atividades_aéreas':, 'endereço_sede':, 'telefone':, 'e-mail':,
# 'decisão_operacional':, 'data_decisão_operacional':, 'validade_operacional':
