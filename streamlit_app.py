import streamlit as st
import subprocess
import numpy

st.info("Sucess!")

"# Run subprocess"
code_1 = st.text_input("Code:", "ls")
output = subprocess.check_output(code_1, shell=True)
st.code(output.decode("utf-8"))

"# Run another subprocess"
code_2 = st.text_input("More code:", "ls")
output = subprocess.check_output(code_2, shell=True)
st.code(output.decode("utf-8"))
