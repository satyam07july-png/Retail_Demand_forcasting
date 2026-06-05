import os
import sys
import pandas as pd

from sklearn.model_selection import train_test_split

from src.utils.exception import CustomException
from src.utils.logger import logging


class DataIngestion:

    def __init__(self):

        self.raw_data_path = os.path.join(
            "data",
            "raw",
            "walmart.csv"
        )

        self.train_data_path = os.path.join(
            "data",
            "processed",
            "train.csv"
        )

        self.test_data_path = os.path.join(
            "data",
            "processed",
            "test.csv"
        )

    def initiate_data_ingestion(self):

        logging.info("Data Ingestion Started")

        try:

            print("\nReading Dataset...")

            df = pd.read_csv(self.raw_data_path)

            print(f"Dataset Loaded Successfully")
            print(f"Shape: {df.shape}")

            logging.info(
                f"Dataset Loaded Successfully. Shape: {df.shape}"
            )

            os.makedirs(
                os.path.dirname(self.train_data_path),
                exist_ok=True
            )

            train_set, test_set = train_test_split(
                df,
                test_size=0.20,
                random_state=42
            )

            train_set.to_csv(
                self.train_data_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.test_data_path,
                index=False,
                header=True
            )

            logging.info("Train and Test files saved")

            print(
                f"\nTrain file saved at: {self.train_data_path}"
            )

            print(
                f"Test file saved at: {self.test_data_path}"
            )

            print(
                f"Train Exists: {os.path.exists(self.train_data_path)}"
            )

            print(
                f"Test Exists: {os.path.exists(self.test_data_path)}"
            )

            logging.info("Data Ingestion Completed Successfully")

            return (
                self.train_data_path,
                self.test_data_path
            )

        except Exception as e:

            logging.error(str(e))

            raise CustomException(
                e,
                sys
            )


if __name__ == "__main__":

    print("\nStarting Data Ingestion...\n")

    obj = DataIngestion()

    train_path, test_path = obj.initiate_data_ingestion()

    print("\nProcess Completed Successfully!")