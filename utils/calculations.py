def calculate_revenue(df):

    return (
        df["Quantity"] *
        df["Price"]
    ).sum()


def total_orders(df):

    return len(df)


def top_executive(df):

    df["Revenue"] = (
        df["Quantity"] *
        df["Price"]
    )

    result = df.groupby(
        "Executive"
    )["Revenue"].sum()

    return result.idxmax()


def top_customer(df):

    df["Revenue"] = (
        df["Quantity"] *
        df["Price"]
    )

    result = df.groupby(
        "Customer"
    )["Revenue"].sum()

    return result.idxmax()