"""Meeting 7 student starter. See docs/LABS.md. This is intentionally unfinished."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Ask Your Sales Data')
st.title('Ask Your Sales Data')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Read and validate the sales CSV.
st.write('1. Read and validate the sales CSV.')
# TODO 2: Use summarise() and display the exact facts supplied to AI.
st.write('2. Use summarise() and display the exact facts supplied to AI.')
# TODO 3: Collect a bounded question in a form.
st.write('3. Collect a bounded question in a form.')
# TODO 4: Explain unsupported questions; never execute model-generated code.
st.write('4. Explain unsupported questions; never execute model-generated code.')
