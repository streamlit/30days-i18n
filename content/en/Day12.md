# st.checkbox

`st.checkbox` displays a checkbox widget.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## Code
Here's how to use `st.checkbox`:
```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

This is followed by creating a header text for the app:
```python
st.header('st.checkbox')
```

Next, we're going to ask a question via `st.write':
```python
st.write ('What would you like to order?')
```

We're then going to provide some menu items to tick on:
```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

Finally, we're going to print custom text depending on which checkbox was ticked on:
```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## Further reading
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
