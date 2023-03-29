# st.file_uploader

`st.file_uploader` displays a file uploader widget [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option. For more info on how to set config options, see [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## Code
Here's how to use `st.file_uploader`:
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` and other prerequisite library like so:
```python
import streamlit as st
import pandas as pd
```

This is followed by creating a title text for the app:
```python
st.title('st.file_uploader')
```

Next, we'll use `st.file_uploader` to display a file uploader widget for accepting user input file:
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

Finally, we define conditional statements for initially displaying a welcome message inviting users to upload their file (as implemented in the `else` condition). Upon file upload, the `if` statements are activated and the CSV file is read by the `pandas` library and displayed via the `st.write` command.
```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Further reading
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Set configuration options](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
