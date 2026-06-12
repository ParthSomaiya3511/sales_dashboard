import streamlit as st

from utils.data_handler import load_data
from utils.calculations import *

df = load_data()

revenue = calculate_revenue(df)

orders = total_orders(df)

executive = top_executive(df)

customer = top_customer(df)

st.title(
    "📊 Sales Executive Dashboard"
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Revenue",
    f"₹{revenue:,.0f}"
)

col2.metric(
    "Orders",
    orders
)

col3.metric(
    "Top Executive",
    executive
)

col4.metric(
    "Top Customer",
    customer
)

st.dataframe(df)