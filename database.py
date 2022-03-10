import sqlite3

conn = sqlite3.connect('eleflow')
cursor = conn.cursor()


def table_air_cia():
    cursor.execute(
        """CREATE TABLE air_cia(
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


def table_vra():
    cursor.execute(
        """CREATE TABLE vra(
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


def table_aerodramos():
    cursor.execute(
        """CREATE TABLE aerodramos(
        iata VARCHAR(4),
        icao VARCHAR(4) , 
        name VARCHAR(255),
        location VARCHAR(255),
        street_number INT,
        street VARCHAR(150),
        city VARCHAR(150),
        county VARCHAR(100),
        state VARCHAR(100),
        country_iso VARCHAR(3),
        country VARCHAR(100),
        postal_code VARCHAR(9),
        phone VARCHAR(20),
        latitude DECIMAL,
        longitude DECIMAL,
        uct INT,
        website VARCHAR(255)
    );"""

    )
    def values_air_cia(self, *args):

        cursor.execute(f"""INSERT INTO air_cia(razao_social,icao,iata,cnpj,atividades_aereas,endereco_sede,telefone,
            email, decisao_operacional,data_decisao_operacional,validade_operacional) VALUES('{args[0]}','{args[1]}','{args[2]}','{args[3]}',
            '{args[4]}','{args[5]}','{args[6]}','{args[7]}','{args[8]}','{args[9]}','{args[10]}'); """
                       )
        conn.commit()
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

if __name__ == '__main__':

    #table_air_cia()
    #table_vra()
    #table_aerodramos()
    cursor.execute('drop table air_cia ')

    # engine = db.create_engine('dialect+driver://user:pass@host:port/db')
