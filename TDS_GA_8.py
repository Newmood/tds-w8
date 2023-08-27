# TDS GA 8

import streamlit as st

st.title("Largest of Three")

st.write("Please enter three numbers one by one")

n1 = st.number_input("Enter the first number:")
n2 = st.number_input("Enter the second number:")
n3 = st.number_input("Enter the third number:")

if st.button("Get the largest number"):
    nl= max(n1,n2,n3)
    st.success(f"The largest number is: {nl}")