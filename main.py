from src.data_preparation.extract_data import extract_data
from src.data_preparation.load_data import load_data
from src.data_preparation.clean_data import clean_data
from src.data_preparation.transform_data import transform_data
from src.dashboard.dashboard import dashboard

extract_data()
load_data()
clean_data()
transform_data()
dashboard()


