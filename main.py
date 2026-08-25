from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__ == "__main__":
    try:
        # Create training pipeline configuration
        trainingpipelineconfig = TrainingPipelineConfig()

        # Create data ingestion configuration
        dataingestionconfig = DataIngestionConfig(
            training_pipeline_config=trainingpipelineconfig
        )

        # Create DataIngestion object
        data_ingestion = DataIngestion(
            data_ingestion_config=dataingestionconfig
        )

        logging.info("Initiate Data Ingestion")

        # Start data ingestion
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate Data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

       

    except Exception as e:
        raise NetworkSecurityException(e, sys)