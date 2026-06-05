import pandas as pd

class FeatureEngineering:

   def create_features(self, df):

       df['Date'] = pd.to_datetime(df['Date'])

       df['day'] = df['Date'].dt.day
       df['month'] = df['Date'].dt.month
       df['year'] = df['Date'].dt.year
       df['week'] = df['Date'].dt.isocalendar().week
       df['dayofweek'] = df['Date'].dt.dayofweek

       # Lag Features
       df['lag_7'] = df['Weekly_Sales'].shift(7)

       # Rolling Mean
       df['rolling_mean_7'] = (
           df['Weekly_Sales']
           .rolling(window=7)
           .mean()
       )

       df.fillna(0, inplace=True)

       return df