import os
import pandas as pd
import sys

from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

from src.components.data_tranformation import DataTransformation,DataTransformationConfig
"""The main purpose of the this file to read data from source and do train
test split and save in to artifacts"""
@dataclass
class DataIngestionConfig:
    # helpful if we declare the variables only
    train_data_path: str= os.path.join('artifacts',"train.csv")
    test_data_path: str= os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r"src\notebook\data\stud.csv")
            logging.info('Read the dataset as df')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2, random_state=42)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False, header=True)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            logging.info("Ingestion of the data is completed")
            
            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr, test_arr,preprocessor_obj_file_path=data_transformation.initiate_data_transformation(train_data,test_data)
    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))