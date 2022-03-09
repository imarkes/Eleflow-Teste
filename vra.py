import glob
import json
from msilib.schema import Patch
import os
import re

path = 'VRA'

class FilesVRA:
    def __init__(self, path) -> None:
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

        with open(file_json, encoding='utf-8-sig') as f_json:
            read_data = json.load(f_json)

            for data in read_data:
                headers = list(data)
                new_header = [self.convert_words_for_snake_case(words) for words in headers]

                values = list(data.values())
                new_json = dict(zip(new_header, values))
                return new_json

    def read_all_files_in_path(self):
        """Return generator object FilesVRA."""
        for files in self.vra_files_json:
            yield self.normalizer_headers(files)


if __name__ == '__main__':
    a = FilesVRA(path)
    print(list(a.read_all_files_in_path()))