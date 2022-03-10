import csv
import json
import sqlite3


class Engine:
    def __init__(self):
        self.conn = sqlite3.connect('eleflow')  # Cria database.
        self.cursor = self.conn.cursor()


class TableAirCia(Engine):
    def __init__(self):
        Engine.__init__(self)
        self.table_air_cia()

    def table_air_cia(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS air_cia(
            razao_social VARCHAR(150), 
            icao VARCHAR(3),
            iata VARCHAR(2),
            cnpj VARCHAR(18) ,
            atividades_aereas VARCHAR(30),
            endereco_sede VARCHAR(255),
            telefone VARCHAR(70),
            email VARCHAR(50),
            decisao_operacional VARCHAR(20),
            data_decisao_operacional DATE,
            validade_operacional DATE,
            add_data DATETIME default CURRENT_TIMESTAMP
        ); """
        )

    def values_air_cia(self, *args):

        self.cursor.execute(f"""INSERT INTO air_cia(razao_social,icao,iata,cnpj,atividades_aereas,endereco_sede,telefone,
            email, decisao_operacional,data_decisao_operacional,validade_operacional) VALUES('{args[0]}','{args[1]}','{args[2]}','{args[3]}',
            '{args[4]}','{args[5]}','{args[6]}','{args[7]}','{args[8]}','{args[9]}','{args[10]}'); """
                            )
        self.conn.commit()
        print('Dados inseridos com sucesso.')

    def read_csv(self, filename):
        """Ler o arquivo e insere as linhas no banco de dados."""
        try:
            FILE_CSV = csv.DictReader(open(filename, encoding='utf-8'))

            for row in FILE_CSV:
                self.values_air_cia(row['razão_social'], row['icao'], row['iata'], row['cnpj'],
                                    row['atividades_aéreas'],
                                    row['endereço_sede'], row['telefone'], row['e-mail'],
                                    row['decisão_operacional'], row['data_decisão_operacional'],
                                    row['validade_operacional']
                                    )

                print('Success')

        except ConnectionError as e:
            print(f'Erro ao inserir os dados: Func: insert_csv: Error: {e}')
            return e


class TableVRA(Engine):
    def __init__(self):
        Engine.__init__(self)
        self.table_vra()

    def table_vra(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS vra(
            icaoempresa_aerea VARCHAR(3) ,
            numero_voo VARCHAR(9),
            codigo_autorizacao VARCHAR(2), 
            codigo_tipo_linha VARCHAR(2),
            icaoaerodromo_origem VARCHAR(5),
            icaoaerodromo_destino VARCHAR(5),
            partida_prevista DATETIME, 
            partida_real DATETIME,
            chegada_prevista DATETIME,
            chegada_real DATETIME,
            situacao_voo VARCHAR(10), 
            codigo_justificativa VARCHAR(3),
            add_data DATETIME default CURRENT_TIMESTAMP    
            );"""
        )

    def save_values_vra(self, *args):

        self.cursor.execute(f"""INSERT INTO vra(icaoempresa_aerea,numero_voo,codigo_autorizacao,codigo_tipo_linha,
        icaoaerodromo_origem,icaoaerodromo_destino,partida_prevista, partida_real, chegada_prevista,chegada_real,
        situacao_voo, codigo_justificativa) VALUES('{args[0]}','{args[1]}','{args[2]}','{args[3]}', 
            '{args[4]}','{args[5]}','{args[6]}','{args[7]}','{args[8]}','{args[9]}','{args[10]}', '{args[10]}'); """
                            )
        self.conn.commit()
        print('Dados inseridos com sucesso.')

    def read_json(self, filename):
        """Ler o arquivo e insere as linhas no banco de dados."""
        try:
            with open(filename, encoding='utf-8') as VRA_json:
                data_json = json.load(VRA_json)

            for row in data_json:
                self.save_values_vra(row['icaoempresa_aérea'], row['número_voo'], row['código_autorização'],
                                     row['código_tipo_linha'], row['icaoaeródromo_origem'],
                                     row['icaoaeródromo_destino'], row['partida_prevista'], row['partida_real'],
                                     row['chegada_prevista'], row['chegada_real'],
                                     row['situação_voo'], row['código_justificativa']
                                     )

                print('Success')

        except ConnectionError as e:
            print(f'Erro ao inserir os dados: Func: insert_csv: Error: {e}')
            return e


class TableAerodramos(Engine):
    def __init__(self):
        Engine.__init__(self)
        self.table_aerodramos()

    def table_aerodramos(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS aerodramos(
            id INT PRIMARY KEY, 
            iata VARCHAR(5),
            icao VARCHAR(5) , 
            name VARCHAR(255),
            location VARCHAR(255),
            street_number VARCHAR(15),
            street VARCHAR(150),
            city VARCHAR(150),
            county VARCHAR(150),
            state VARCHAR(1150),
            country_iso VARCHAR(5),
            country VARCHAR(150),
            postal_code VARCHAR(20),
            phone VARCHAR(25),
            latitude DECIMAL,
            longitude DECIMAL,
            uct INT,
            website VARCHAR(255)
        );""")

    def values_aerodramos(self, *args):
        self.cursor.execute(f"""INSERT INTO aerodramos(id, iata, icao, name, location, street_number, street, city, 
        county, state, country_iso, country, postal_code, phone, latitude, longitude, uct, website) VALUES({args[0]},
        '{args[1]}','{args[2]}','{args[3]}','{args[4]}','{args[5]}','{args[6]}','{args[7]}', 
                '{args[8]}','{args[9]}','{args[10]}','{args[11]}','{args[12]}','{args[13]}',{args[14]},{args[15]},
                {args[16]},'{args[17]}')""")

        self.conn.commit()
        print('Dados inseridos com sucesso.')

    def read_csv(self, filename):
        """Ler o arquivo e insere as linhas no banco de dados."""
        try:
            data_csv = csv.DictReader(open(filename, encoding='utf-8'))

            for row in data_csv:
                self.values_aerodramos(row['id'], row['iata'], row['icao'], row['name'], row['location'],
                                       row['street_number'], row['street'], row['city'], row['county'],
                                       row['state'], row['country_iso'], row['country'], row['postal_code'],
                                       row['phone'], row['latitude'], row['longitude'], row['uct'], row['website']
                                       )
                print('Success')

        except ConnectionError as e:
            print(f'Erro ao inserir os dados: Func: insert_csv: Error: {e}')
            return e


if __name__ == '__main__':
    ...
    air_cia = TableAirCia()
    air_cia.read_csv('FilesAirCia/air_cia.csv')

    vra = TableVRA()
    vra.read_json('FilesVRA/vra.json')

    #aerodramos = TableAerodramos()
    #aerodramos.read_csv('Aerodromos/aerodromos.csv')

    #Engine().cursor.execute('drop table aerodramos ')
