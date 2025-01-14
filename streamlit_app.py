import streamlit as st
import pandas as pd

st.title("Survey of Construction 2023")
st.write(
    "Investigation of the 2023 [US Census Bureau Survey of Construction](https://www.census.gov/construction/soc/index.html)."
)

data = pd.read_csv("soc2023.csv")
vars = pd.read_csv("soc_variables.csv")

data_options = sorted(vars["Description"].to_list())

x_label = st.selectbox("X axis", options=data_options, index=data_options.index("Square Foot Area of House"))
x_key = vars.loc[vars["Description"] == x_label, "Variable"].values[0]
st.text(vars.loc[vars["Description"] == x_label, "Possible Values"].values[0])

y_label = st.selectbox("Y axis", options=data_options, index=data_options.index("Final Sales Price at Completion"))
y_key = vars.loc[vars["Description"] == y_label, "Variable"].values[0]
st.text(vars.loc[vars["Description"] == y_label, "Possible Values"].values[0])


drop_na = st.checkbox("Drop missing values", value=True)
if drop_na:
    data = data.drop(data[(data[x_key] <= 0) | (data[y_key] <= 0)].index)

st.scatter_chart(data, x=x_key, x_label=x_label, y=y_key, y_label=y_label)