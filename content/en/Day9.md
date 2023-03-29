# st.line_chart

`st.line_chart` displays a line chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If `st.line_chart` does not guess the data specification correctly, try specifying your desired chart using st.altair_chart.

## What we're building?

A simple app for displaying a line chart.

Flow of the app:
1. Create a `Pandas` DataFrame from numbers randomly generated via `NumPy`.
2. Create and display the line chart via `st.line_chart()` command.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Code
Here's how to use [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` as well as other libraries like so:
```python
import streamlit as st
import pandas as pd
import numpy as np
```

Next, we create a header text for the app:
```python
st.header('Line chart')
```

Then, we create a DataFrame of randomly generated numbers that contains 3 columns.
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Finally, a line chart is created by using `st.line_chart()` with the DataFrame stored in the `chart_data` variable as  the input data:
```python
st.line_chart(chart_data)
```

## Further reading
Read more about the following related Streamlit command from which [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) is based on:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
