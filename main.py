import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")



df  = pd.read_csv("sp500_top10_stocks_clean.csv")

print(df.head())
print("Data Load sucessfully....")
print("Dataset shape ",df.shape)
print("\nColumns name ",df.columns.to_list())
print("Data type ",df.dtypes)
print("\nBasic statistics ",df.describe())



# step 1 : Date datatype fix 
df["Date"] = pd.to_datetime(df["Date"],errors="coerce")
print(df["Date"].dtype)
# print(df.dtypes)

# step 2 : create a column daily return
df = df.sort_values(["Ticker","Date"])
df["Daily_return"] = df.groupby("Ticker")["Adj_Close"].pct_change() * 100
print(df.dtypes)
print("Total NaN is daily return ",df["Daily_return"].isna().sum())
# we fill nan values with 0 in daily return col
print("daily return column fill with 0 ")
df["Daily_return"] = df["Daily_return"].fillna(0)
print("Total NaN is daily return ",df["Daily_return"].isna().sum())


# create a one column daily price difference 
df["Price_change"] = df["Close"] - df["Open"]

# create a one column high low difference
df["HL_diff"] = df["High"] - df["Low"]

print(df.shape)
print(df)

# clean csv import clean_sp500_top10_stock.csv
df.to_csv("clean_sp500_top10_stock.csv",index="False")
print("New clean csv clean clean_sp500_top10_stock.csv")