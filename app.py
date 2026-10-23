
import streamlit as st

st.set_page_config(
    page_title="Snow-kNOw",
    page_icon="❄️",
    layout="wide"
)

st.title("❄️ Snow-kNOw")
st.subheader("Plan your perfect ski holiday")

st.write(
    "Find ski destinations with reliable snow "
    "conditions and plan your next winter holiday."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎿 Ski Holiday Planner")
    st.write(
        "Discover ski destinations and compare "
        "snow conditions."
    )

with col2:
    st.subheader("🏡 Holiday Home Advisor")
    st.write(
        "Find the right region for your future "
        "holiday home."
    )

st.info(
    "Use the navigation menu on the left "
    "to explore Snow-kNOw."
)
