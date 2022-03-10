import csv
import glob
import json
import os
import re


class FilesVRA:
    def __init__(self, path='VRA') -> None:
        self.all_files = None
        self.path = path
        self.vra_files_json = glob.glob(os.path.join(path, '*.json'))

    def convert_words_for_snake_case(self, words: str) -> str:
        """
        :param: IvanMarques
        :return: ivan_marques
        """
        assert isinstance(words, str)

        words = re.findall('[A-Z]*[^A-Z]*', words)  # split letras maiúsculas
        words = [x.lower() for x in words]

        return '_'.join(words)[:-1]

    def normalizer_headers(self, file_json: list) -> list:
        """
        :param: [IvanMarques, DevPython]
        :return: [ivan_marques, dev_python]
        """

        try:
            with open(file_json, encoding='utf-8-sig') as f_json:
                read_data = json.load(f_json)

                for data in read_data:
                    headers = list(data)
                    new_header = [self.convert_words_for_snake_case(words) for words in headers]

                    values = list(data.values())
                    new_json = dict(zip(new_header, values))
                    yield new_json

        except Exception as e:
            print(f'Não foi possivel normalizar os dados. Error: {e}')

    def read_all_files_in_path(self):
        """Return all files normalized."""
        try:
            for files in self.vra_files_json:
                self.all_files = list(self.normalizer_headers(files))
                return self.all_files

        except Exception as e:
            print(f'Não foi possivel ler o diretório dados. Error: {e}')

    def generate_file_json(self):
        """Generate json file."""
        try:
            with open('vra.json', mode='w', encoding='utf-8') as outfile:
                json.dump(self.all_files, outfile, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f'Não foi possivel gerar o arquivo Json. Error: {e}')

    def create_dir_new_files(self, path):
        """Create dir path new files."""
        assert isinstance(path, str)

        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)


if __name__ == '__main__':
    ...
    # a = FilesVRA()
    # a.read_all_files_in_path()
    # a.create_dir_new_files('FilesVRA')
    # a.generate_file_json()
