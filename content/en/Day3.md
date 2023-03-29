# st.button

`st.button` allows the display of a button widget.

## What we're building?

A simple app that performs conditionally prints out alternative messages depending on whether the button was pressed or not.

Flow of the app:

1. By default, the app prints `Goodbye`
2. Upon clicking on the button, the app displays the alternative message `Why hello there`

## Demo app

The deployed Streamlit app should look something like the one shown in the below link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Code

Here's the code to implement the above mentioned app:

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## Line-by-line explanation

The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:

```python
import streamlit as st
```

This is followed by creating a header text for the app:

```python
st.header('st.button')
```

Next, we will use conditional statements `if` and `else` for printing alternative messages.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

As we can see from the above code box, the `st.button()` command accepts the `label` input argument of `Say hello`, which is the text that the button displays.

The `st.write` command is used to print text messages of either `Why hello there` or `Goodbye` depending on whether the button was clicked or not, which is implemented via:


```python
st.write('Why hello there')
```

and

```python
st.write('Goodbye')
```

It is important to note that the above `st.write` statements are placed under the `if` and `else` conditions in order to perform the above mentioned process of alternative displaying of messages

## Next steps

Now that you have created the Streamlit app locally, it's time to deploy it to [Streamlit Community Cloud](https://streamlit.io/cloud) as will be explained soon in an upcoming challenge.

Because this is the first week of your challenge, we provide the full code (as shown in the code box above) and solution (the demo app) right inside this webpage.

Moving forward in the next challenges, it is recommended that you first try implementing the Streamlit app yourself.

Don't worry if you get stuck, you can always take a peek at the solution.

## References

Read about [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) in the Streamlit API Documentation.
