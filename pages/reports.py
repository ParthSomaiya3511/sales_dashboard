import streamlit as st

from utils.data_handler import load_data

df = load_data()

st.title(
    "📄 Sales Reports"
)

st.dataframe(df)

csv = df.to_csv(
    index=False
)

st.download_button(
    "Download CSV",
    csv,
    file_name="sales_report.csv",
    mime="text/csv"
)