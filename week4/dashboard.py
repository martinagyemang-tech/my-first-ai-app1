"""Meeting 6 student starter. See docs/LABS.md. This is intentionally unfinished."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Sales Dashboard')
st.title('Sales Dashboard')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Load sample/uploaded data with sales_input().
st.write('1. Load sample/uploaded data with sales_input().')
# TODO 2: Validate before calculating; stop if no valid data.
st.write('2. Validate before calculating; stop if no valid data.')
# TODO 3: Show verified metrics, grouped results and a chart.
st.write('3. Show verified metrics, grouped results and a chart.')
# TODO 4: Generate an explanation only on button click; clear it when facts change.
st.write('4. Generate an explanation only on button click; clear it when facts change.')
