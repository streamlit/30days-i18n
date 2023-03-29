# st.secrets

`st.secrets` allows you to store confidential information such as API keys, database passwords or other credentials.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## Code
Here's how to use `st.secrets`:
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

This is followed by creating a title text for the app:
```python
st.title('st.secrets')
```

Finally, we'll be displaying the stored secrets:
```python
st.write(st.secrets['message'])
```

It should be noted that, secrets can be stored in Streamlit Community Cloud as shown in the screenshots shown below.

If working locally, they can be stored in `.streamlit/secrets.toml`, but make sure to avoid uploading this to a GitHub repo when deploying the app.

## Further reading
- [Add secrets to your Streamlit apps](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Secrets management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
