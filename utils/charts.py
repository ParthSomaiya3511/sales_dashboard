import plotly.express as px

def revenue_chart(df):

    df["Revenue"] = (
        df["Quantity"] *
        df["Price"]
    )

    chart = px.bar(
        df,
        x="Executive",
        y="Revenue",
        title="Sales Revenue"
    )

    return chart


def product_chart(df):

    chart = px.pie(
        df,
        names="Product",
        title="Product Sales"
    )

    return chart