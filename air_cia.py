import csv
import glob
import os


class FilesAIRCIA:
    def __init__(self, path='AIR_CIA') -> None:
        self.path = path
        self.csv_files = glob.glob(os.path.join(path, '*.csv'))

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

                new_dict = dict(zip(headers, new_values))

                return new_dict

    def read_all_files_in_path(self):
        """Return generator object FilesAIRCIA."""

        for files in self.csv_files:
            yield self.normalize_readers_csv(files)


if __name__ == '__main__':
    a = FilesAIRCIA()
    print(list(a.read_all_files_in_path()))
