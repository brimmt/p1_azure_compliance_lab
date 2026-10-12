import streamlit as st
from excel_logic import export_compliance_results
from baseline_logic import update_results_list
from pathlib import Path


st.title("Compliance Results")
if "results" not in st.session_state:
    st.session_state.results = []

if "filename" not in st.session_state:
    st.session_state.filename = None



if st.button("Run Compliance Check"):
    
    with st.spinner("Running compliance check"):
        st.session_state.results = update_results_list()

    st.session_state.filename = None
    
    if st.session_state.results: 
        st.success("Compliance check completed!")
        st.dataframe(st.session_state.results)
        


    if st.button("Generate Excel Report"):
        filename = export_compliance_results(
            st.session_state.results
        )
        st.session_state.filename = filename



    if st.session_state.filename:

            filename = st.session_state.filename

            st.download_button(
                label="Download Report",
                data=Path(filename).read_bytes(),
                file_name=Path(filename).name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )