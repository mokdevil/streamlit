import streamlit as st
import time
import numpy as np

# Define the SessionState class for persisting variables
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Check if session_state exists, otherwise initialize it
if 'session_state' not in st.session_state:
    st.session_state['session_state'] = SessionState(test=False, generated_data=[], last_generated=None)

st.write("""This demo illustrates a combination of plotting and animation with Streamlit.
We're generating a bunch of random numbers in a loop for around 5 seconds. Enjoy!
""")

# If it's the first run or the "Re-run" button has been clicked
if not st.session_state['session_state'].test:
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    # Generate and update the chart for 100 iterations
    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(10, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        st.session_state['session_state'].generated_data.extend(new_rows)
        st.session_state['session_state'].last_generated = new_rows[-1][0]
        last_rows = new_rows
        time.sleep(0.05)
        progress_bar.empty()

    # Set the 'test' flag to True to indicate the first run is completed
    st.session_state['session_state'].test = True

# If it's a subsequent run (after the first run or when the "Re-run" button is clicked)
elif st.session_state['session_state'].test:
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.array([[st.session_state['session_state'].last_generated]])

    # Generate and update the chart for 100 iterations, starting from the last generated number
    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(10, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        st.session_state['session_state'].generated_data.extend(new_rows)
        st.session_state['session_state'].last_generated = new_rows[-1][0]
        last_rows = new_rows
        time.sleep(0.05)
        progress_bar.empty()

    # Display the chart with the previously generated data
    st.line_chart(st.session_state['session_state'].generated_data)

# Button to rerun the app
st.button("Re-run")