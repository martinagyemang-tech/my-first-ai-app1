"""Shared UI plumbing. Each app keeps its learning-specific logic visible."""
from pathlib import Path
import streamlit as st
from coursekit.ai import settings, reply, AIError
from coursekit.sales import load_sales


def configuration():
    # File/environment configuration only; visitors cannot switch on billable mode.
    try:
        values = dict(st.secrets)
    except FileNotFoundError:
        values = {}
    config = settings(values)
    st.caption('Practice mode: fixed responses; no AI calls.' if config['APP_MODE'] == 'demo'
               else 'Live AI mode: questions and the stated context are sent to OpenAI.')
    return config


def request(messages, instructions, config):
    count = st.session_state.get('api_requests', 0)
    if count >= 20:
        st.error('This session has reached its 20-request teaching limit.')
        return None
    # Count attempts, not just successes. This is NOT a global spending cap.
    st.session_state.api_requests = count + 1
    try:
        with st.spinner('Preparing the response...'):
            return reply(messages, instructions, config)
    except AIError as exc:
        st.error(str(exc))
        return None


def sales_input():
    sample = st.checkbox('Use the sample sales data', value=True)
    if sample:
        raw = (Path(__file__).resolve().parents[1] / 'data' / 'sales.csv').read_bytes()
    else:
        st.caption('Practice data only. Required columns: product, region, units, revenue. Maximum 1 MB / 2,000 rows.')
        uploaded = st.file_uploader('Sales CSV', type=['csv'])
        if uploaded is None:
            st.info('Upload a CSV to continue.')
            return None
        if uploaded.size > 1_000_000:
            st.error('Use a CSV up to 1 MB.')
            return None
        raw = uploaded.getvalue()
    try:
        return load_sales(raw)
    except ValueError as exc:
        st.error(str(exc))
        return None
