# st.session_state

We define access to a Streamlit app in a browser tab as a session. For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app. Each reruns takes place in a blank slate: no variables are shared between runs.

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks.

In this tutorial, we will illustrate the usage of Session State and Callbacks as we build a weight conversion app.

`st.session_state` allows the implementation of session state in a Streamlit app.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## Code
Here's how to use `st.session_state`:
```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

Firstly, we'll start by creating the title of the app:
```python
st.title('st.session_state')
```

Next, we define custom functions for the weight conversion from lbs to kg and vice versa:
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

Here, we use `st.number_input` to accept numerical inputs of the weight values:
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```
The above 2 custom functions will be called upon as soon as a numerical value is entered into the number box created using the `st.number_input` command. Notice how the `on_change` option specifies the 2 custom functions `lbs_to_kg` and `kg_to_lbs`). 

In a nutshell, upon entering a number into the `st.number_input` box the number is converted by these custom functions.

Finally, the weight values in `kg` and `lbs` units as stored in the session state as `st.session_state.kg` and `st.session_state.lbs` will be printed out via `st.write`:
```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Further reading
- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [Add statefulness to apps](https://docs.streamlit.io/library/advanced-features/session-state)
