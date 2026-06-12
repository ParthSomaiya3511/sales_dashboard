import streamlit as st

from utils.data_handler import save_sale

st.title(
    "➕ Add New Sale"
)

date = st.date_input(
    "Date"
)

executive = st.text_input(
    "Executive Name"
)

customer = st.text_input(
    "Customer Name"
)

product = st.selectbox(
    "Product",
    [
        "Laptop",
        "Mobile",
        "Tablet"
    ]
)

quantity = st.number_input(
    "Quantity",
    min_value=1
)

price = st.number_input(
    "Price",
    min_value=1
)

if st.button(
    "Save Sale"
):

    data = {
        "Date": date,
        "Executive": executive,
        "Customer": customer,
        "Product": product,
        "Quantity": quantity,
        "Price": price
    }

    save_sale(data)

    st.success(
        "Sale Added Successfully"
    )