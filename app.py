from src.MLProject.logger import logging 
from src.MLProject.exception import CustomException
import sys
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info('the excution has started')

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingetsion=DataIngestion()
        data_ingetsion.initiate_data_ingestion()
    except Exception as e:
        logging.info('custom exception')
        raise CustomException(e.sys)