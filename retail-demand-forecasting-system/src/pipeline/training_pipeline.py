from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":

   ingestion = DataIngestion()

   ingestion.initiate_data_ingestion()

   trainer = ModelTrainer()

   trainer.initiate_model_training()