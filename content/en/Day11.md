# st.multiselect

`st.multiselect` displays a multiselect widget.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## Code
Here's how to use `st.multiselect`:
```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

This is followed by creating a header text for the app:
```python
st.header('st.multiselect')
```

Next, we're going to use the `st.multiselect` widget to accept input where users will be able to select one or more colors of there choice.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

Finally, we'll write out the selected colors:
```python
st.write('You selected:', options)
```

## Further reading
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
