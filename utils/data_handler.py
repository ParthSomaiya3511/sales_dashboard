import pandas as pd

FILE_PATH = "data/sales.csv"

def load_data():
    return pd.read_csv(FILE_PATH)

def save_sale(data):
    df = load_data()

    new_row = pd.DataFrame([data])

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        FILE_PATH,
        index=False
    )