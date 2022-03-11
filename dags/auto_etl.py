from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator 
from database import TableAerodramos, TableAirCia, TableVRA

def cria_databases():
    air_cia = TableAirCia()
    air_cia.read_csv('FilesAirCia/air_cia.csv')
    
    vra = TableVRA()
    vra.read_json('FilesVRA/vra.json')

    aerodramos = TableAerodramos()
    aerodramos.read_csv('Aerodromos/aerodromos.csv')


with DAG ('eleflow', 
    start_date=datetime(2022,3,11),
    schedule_interval= '1 * * * *',  # execução a cada minuto.
    catchup=False, 
    ) as dag:
 

    cria_databases = PythonOperator(
        task_id='consulta_dados',
        python_callable=cria_databases,
    )

    consulta_dados = SqliteOperator(
        sql= """SELECT r.razao_social,
                a.name,
                a.state,
                a.icao,
                a.country_iso,
                v.icaoaerodromo_origem,
                v.icaoaerodromo_destino,
                v.icaoempresa_aerea,
                CASE
                    WHEN a.icao = v.icaoaerodromo_destino THEN a.name
                    WHEN a.icao = v.icaoaerodromo_origem THEN a.name
                    ELSE a.icao
                END 'aeroportos'
                FROM aerodramos a
                LEFT JOIN vra v on a.icao = v.icaoaerodromo_origem or v.icaoaerodromo_destino or v.icaoempresa_aerea
                LEFT JOIN air_cia r on v.icaoempresa_aerea = r.icao
                GROUP BY r.razao_social
                LIMIT 10;""", 
        sqlite_conn_id='eleflow' # database.
    )

    # Fluxo de execução das tasks
    cria_databases >> consulta_dados