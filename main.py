import csv
import glob
import os

path = 'AIR_CIA'
csv_files = glob.glob(os.path.join(path, '*.csv'))

def trata_cabecalho(filename):

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            headers = list(row)
            ICAO = headers[1].split()[0].lower()
            IATA = headers[1].split()[1].lower()
            new_header = [head.replace(' ', '_').lower() for head in headers]
            new_header[1] = ICAO
            new_header.insert(2, IATA)
            headers = new_header

            new_values = list(row.values())
            values = new_values[1].split() 
            if len(values)==0:
               new_values[1] = None
            else:
               new_values[1] = values[0]
 
            if len(values) <= 1:
               new_values.insert(2, None)
            else:
               new_values.insert(2, values[1])

            new_dict = dict(zip(headers, new_values))    
            print('-'*50)
            print(new_dict)        
            print('-'*50)

for files in csv_files:
   trata_cabecalho(files)