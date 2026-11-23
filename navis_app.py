import json
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Navis API Management Suite",
    page_icon=":ship:",
    layout="wide",
)


@st.cache_data
def load_api_data(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}") from exc
    except OSError as exc:
        raise FileNotFoundError(f"Could not read {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("The JSON root must be an object.")
    return data


def get_list(data: dict, key: str) -> list:
    value = data.get(key, [])
    return value if isinstance(value, list) else []


def safe_get(data: dict, *keys, default=""):
    value = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value if value is not None else default


script_dir = Path(__file__).resolve().parent
default_path = script_dir / "apis.json"

uploaded_file = st.sidebar.file_uploader(
    "Load apis.json",
    type=["json"],
    help="Upload an API catalog JSON file.",
)

data = None
error = None

try:
    if uploaded_file is not None:
        uploaded_data = json.load(uploaded_file)
        if not isinstance(uploaded_data, dict):
            raise ValueError("The JSON root must be an object.")
        data = uploaded_data
    elif default_path.exists():
        data = load_api_data(str(default_path))
except (json.JSONDecodeError, ValueError, FileNotFoundError) as exc:
    error = str(exc)

if error:
    st.error(f"Could not load the API catalog: {error}")

if data is None:
    st.info(
        "Place `apis.json` beside `navis_app.py`, or upload the file from "
        "the sidebar."
    )
    st.stop()

st.sidebar.image(safe_get(data, "image", default=None), width=100)
st.sidebar.title("Navis API Management")
st.sidebar.markdown(
    f"**Specification:** {safe_get(data, 'specificationVersion', default='Unknown')}"
)
st.sidebar.markdown(
    f"**Service model:** {safe_get(data, 'deliveryModel', 'label', default='Unknown')}"
)

apis = get_list(data, "apis")
menu = st.sidebar.radio(
    "Choose a section:",
    [
        "Overview",
        "APIs",
        "Common resources",
        "Raw JSON",
    ],
)

if menu == "Overview":
    st.title(f":ship: {safe_get(data, 'name', default='Navis API Catalog')}")
    st.write(safe_get(data, "description", default=""))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("APIs", len(apis))
    with col2:
        pricing = safe_get(data, "accessModel", "pricing", default="Unknown")
        st.metric("Access model", str(pricing).capitalize())
    with col3:
        delivery = safe_get(data, "deliveryModel", "model", default="Unknown")
        st.metric("Deployment", str(delivery).upper())

    st.subheader("Categories and tags")
    tags = get_list(data, "tags")
    st.write(" ".join(f"`{tag}`" for tag in tags) if tags else "No tags")

    st.subheader("Maintenance team")
    maintainers = get_list(data, "maintainers")
    if maintainers:
        for maintainer in maintainers:
            name = maintainer.get("FN", "Unknown") if isinstance(maintainer, dict) else "Unknown"
            email = maintainer.get("email", "") if isinstance(maintainer, dict) else ""
            st.info(f"**{name}**" + (f" - `{email}`" if email else ""))
    else:
        st.write("No maintainers listed")

elif menu == "APIs":
    st.title("APIs")
    if not apis:
        st.info("No APIs are defined in this catalog.")
    else:
        names = [
            api.get("name", f"API {index + 1}")
            if isinstance(api, dict)
            else f"API {index + 1}"
            for index, api in enumerate(apis)
        ]
        api_selection = st.selectbox("Choose an API", names)
        selected_api = apis[names.index(api_selection)]

        st.subheader(selected_api.get("name", "API"))
        st.write(f"**Description:** {selected_api.get('description', '')}")
        st.write(f"**AID:** `{selected_api.get('aid', '')}`")

        human_url = selected_api.get("humanURL")
        if human_url:
            st.markdown(f"[Visit official website]({human_url})")

        st.markdown("### Related properties")
        properties = get_list(selected_api, "properties")
        if properties:
            for prop in properties:
                if isinstance(prop, dict):
                    st.markdown(
                        f"- **{prop.get('type', 'Property')}:** "
                        f"`{prop.get('url', '')}`"
                    )
        else:
            st.write("No related properties")

elif menu == "Common resources":
    st.title("Common resources")
    common = get_list(data, "common")
    if not common:
        st.info("No common resources are defined in this catalog.")
    else:
        cols = st.columns(2)
        for index, item in enumerate(common):
            if not isinstance(item, dict):
                continue
            url = item.get("url", "")
            col = cols[index % 2]
            with col:
                label = item.get("type", "Resource")
                st.markdown(f"- **{label}:** [{url}]({url})" if url else f"- **{label}**")

else:
    st.title("Raw JSON")
    st.json(data)
