import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataIngestion:
    def __init__(self):
        self.train_data_path = "data/train.csv"
        self.test_data_path = "data/test.csv"

    def initiate_data_ingestion(self):
        df = pd.read_csv("data/loan_data.csv")

        train_set, test_set = train_test_split(
            df, test_size=0.2, random_state=42
        )

        os.makedirs("data", exist_ok=True)

        train_set.to_csv(self.train_data_path, index=False)
        test_set.to_csv(self.test_data_path, index=False)

        return self.train_data_path, self.test_data_path


if __name__ == "__main__":
    obj = DataIngestion()
    train, test = obj.initiate_data_ingestion()
    print(train, test)