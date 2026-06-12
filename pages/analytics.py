import streamlit as st

from utils.data_handler import load_data
from utils.charts import *

df = load_data()

st.title(
    "📈 Sales Analytics"
)

st.plotly_chart(
    revenue_chart(df),
    use_container_width=True
)

st.plotly_chart(
    product_chart(df),
    use_container_width=True
)