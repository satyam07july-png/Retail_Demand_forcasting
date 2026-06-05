from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("artifacts/models/xgboost.pkl")

columns = joblib.load(
   "artifacts/models/model_columns.pkl"
)


@app.get("/")
def home():

   return {
       "message": "Retail Forecast API Running"
   }


@app.post("/predict")
def predict(data: dict):

   df = pd.DataFrame([data])

   df = pd.get_dummies(df)

   df = df.reindex(
       columns=columns,
       fill_value=0
   )

   prediction = model.predict(df)

   return {
       "forecasted_sales": float(prediction[0])
   }