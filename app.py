import streamlit as st
import pandas as pd
import time
from datetime import datetime
import os

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Construct the file path
directory = "F:\facial _recognition\Attendance"
file_name = f"F:\facial _recognition\Attendance_{date}.csv"
file_path = os.path.join(directory, file_name)

# Check if the file exists before attempting to read it
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.write(f"File '{file_name}' not found in directory '{directory}'")
