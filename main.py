from gerators.aerodromos import AerodromosCSV
from gerators.air_cia import FilesAIRCIA
from gerators.vra import FilesVRA


vra = FilesVRA()
vra.read_all_files_in_path()
vra.create_dir_new_files('FilesVRA')
vra.generate_file_json()

air = FilesAIRCIA()
air.read_all_files_in_path()
air.create_dir_new_files('FilesAirCia')
air.generate_csv_air_cia()

icao = AerodromosCSV()
icao.get_codgos_icao('FilesVRA/vra.json')
icao.response_get_url()
icao.create_dir_new_files('Aerodromos')
icao.generate_csv()


