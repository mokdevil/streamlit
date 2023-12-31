import streamlit as st
import pandas as pd

st.title("File uploader test")
st.write("Choose a .py, .jpeg .txt or a .csv file")

uploaded_file = st.file_uploader("Choose a file", type=["py", "jpeg", "txt", "csv"])

@st.cache_data
def read_file(file):
    return file.read().decode("utf-8")

if uploaded_file is not None:
    filename = uploaded_file.name

    if filename.endswith(".py"):
        with uploaded_file as f:
            code_string = read_file(f)
            if st.checkbox("Show source code", False):
                st.code(code_string, language=("python"))
            new_code_string = code_string.replace("st.set_page_config", "#")
            if st.checkbox("Run python script", False):
                exec(new_code_string)

    elif filename.endswith(".txt"):
        with uploaded_file as f:
            op = st.selectbox(
                'Select how to display text',
                ("Text", "Code", "Write"))
            if op == "Text":    
                st.text(read_file(f))
            elif op == "Code":
                st.code(read_file(f))
            elif op == "Write":
                st.write(read_file(f))

    elif filename.endswith(".jpeg"):
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    elif filename.endswith(".csv"):
        rd = pd.read_csv(uploaded_file)
        st.dataframe(rd)