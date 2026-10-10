"""Meeting 3 student starter. See docs/LABS.md. This is intentionally unfinished."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Market Assistant')
st.title('Market Assistant')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Create a form with product, quantity and question inputs.
st.write('1. Create a form with product, quantity and question inputs.')
# TODO 2: Use quote() and display receipt().
st.write('2. Use quote() and display receipt().')
# TODO 3: Call request() only after submission and non-empty question.
st.write('3. Call request() only after submission and non-empty question.')
# TODO 4: Save the result in session state.
st.write('4. Save the result in session state.')
