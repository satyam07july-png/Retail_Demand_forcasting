import joblib
import pandas as pd

from xgboost import XGBRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from src.components.feature_engineering import FeatureEngineering


class ModelTrainer:

   def initiate_model_training(self):

       df = pd.read_csv("data/processed/train.csv")

       feature_obj = FeatureEngineering()

       df = feature_obj.create_features(df)

       X = df.drop(columns=["Weekly_Sales", "Date"])

       y = df["Weekly_Sales"]

       X = pd.get_dummies(X)

       X_train, X_test, y_train, y_test = train_test_split(
           X,
           y,
           test_size=0.2,
           random_state=42
       )

       model = XGBRegressor(
           n_estimators=300,
           learning_rate=0.05,
           max_depth=10
       )

       model.fit(X_train, y_train)

       prediction = model.predict(X_test)

       mae = mean_absolute_error(y_test, prediction)

       print(f"MAE : {mae}")

       joblib.dump(
           model,
           "artifacts/models/xgboost.pkl"
       )

       joblib.dump(
           X.columns,
           "artifacts/models/model_columns.pkl"
       )

       print("Model Saved Successfully")