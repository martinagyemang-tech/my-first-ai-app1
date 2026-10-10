"""Meeting 4 student starter. See docs/LABS.md. This is intentionally unfinished."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Study Buddy')
st.title('Study Buddy')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Initialise messages once with an if-not-in guard.
st.write('1. Initialise messages once with an if-not-in guard.')
# TODO 2: Replay saved user/assistant messages as chat bubbles.
st.write('2. Replay saved user/assistant messages as chat bubbles.')
# TODO 3: Capture a question and call request() with the latest history.
st.write('3. Capture a question and call request() with the latest history.')
# TODO 4: Save successful turns and add a New conversation button.
st.write('4. Save successful turns and add a New conversation button.')
