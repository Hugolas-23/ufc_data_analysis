import zipfile
import os

def extract_data():
    caminho_zip = r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\raw\ufc-events-data-till-2023.zip'
    destino = r'C:\Users\hugom\PycharmProjects\ufc_data_analysis\data\raw'

    if not os.path.exists(caminho_zip):
        raise FileNotFoundError(f'Arquivo {caminho_zip} não encontrado')

    with zipfile.ZipFile(caminho_zip, 'r') as extract:
        extract.extractall(destino)
        print("Arquivos Extraídos")
