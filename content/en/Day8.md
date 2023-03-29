# st.slider

`st.slider` allows the display of a slider input widget.

The following data types are supported: int, float, date, time, and datetime.

## What we're building?

A simple app that shows the various ways on how to accept user input by adjusting the slider widget.

Flow of the app:
1. User selects value by adjusting the slider widget
2. App prints out the selected value

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## Code
Here's how to use st.slider:

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
from datetime import time, datetime
```

This is followed by creating a header text for the app:
```python
st.header('st.slider')
```

**Example 1**

Slider:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

As we can see, the `st.slider()` command
is used to collect user input about the age of users.

The first input argument displays the text just above the **slider** widget asking `'How old are you?'`.

The following three integers `0, 130, 25` represents the minimum, maximum and default values, respectively.

**Example 2**

Range slider:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

The range slider allow selection of a lower and upper bound value pair.

The first input argument displays the text just above the **range slider** widget asking `'Select a range of values'`.

The following three arguments `0.0, 100.0, (25.0, 75.0)` represents the minimum and maximum values while the last tuple denotes the default values to use as the selected lower (25.0) and upper (75.0) bound values.

**Example 3**

Range time slider:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

The range time slider allows selection of a lower and upper bound value pair of datetime.

The first input argument displays the text just above the **range time slider** widget asking `'Schedule your appointment:`.

The default values for the lower and upper bound value pairs of datetime are set to 11:30 and 12:45, respectively.

**Example 4**

Datetime slider:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

The datetime slider allows selection of a datetime.

The first input argument displays the text just above the **datetime** slider widget asking `'When do you start?'`.

The default value for the datetime was set using the `value` option to be January 1, 2020 at 9:30

## Further reading
You can also explore the following related widget:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
