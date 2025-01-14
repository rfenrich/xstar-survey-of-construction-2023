import streamlit as st
import pandas as pd

st.title("Survey of Construction 2023")
st.write(
    "Investigation of the 2023 US Census Bureau Survey of Construction."
)

data = pd.read_csv("soc2023.csv")

st.scatter_chart(data, x="FSQFS", x_label="Square Foot Area", y="SLPR", y_label="Sales Price")
