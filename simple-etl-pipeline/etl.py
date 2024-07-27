import pandas as pd

SOURCE_PATH = "data/staging"
TARGET_PATH = "data/transformed"
FILE = "power_consumption.csv"


def extract(file):
    return pd.read_csv(f"{SOURCE_PATH}/{file}")


def transform(temp_df):
    temp_df["DateTime"] = pd.to_datetime(temp_df["DateTime"])
    temp_df = temp_df.groupby(temp_df["DateTime"].dt.date).mean().round(2).drop(columns=["DateTime"], axis=1).rename(columns={"DateTime": "Date"}).reset_index()
    return temp_df


def load(temp_df):
    temp_df.to_csv(f"{TARGET_PATH}/transformed_{FILE}", index=False, mode="w")
    print(f"Target Shape: {temp_df.shape}")


try:
    df = extract(FILE)
    t_df = transform(df)
    load(t_df)
    print("ETL success!")

except Exception as e:
    print(e)


