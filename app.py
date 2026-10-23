
import streamlit as st

st.set_page_config(
    page_title="Snow-kNOw",
    page_icon="❄️",
    layout="wide"
)

st.title("Snow-kNOw")
st.subheader("Find your best week on snow.")

st.write(
    "Make smarter ski holiday decisions "
    "with snow reliability insights."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("Ski Holiday Planner")
    st.write("Find the right resort for your ski week.")

with col2:
    st.header("Holiday Home Advisor")
    st.write("Explore future snow reliability.")
