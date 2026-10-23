
import streamlit as st

st.set_page_config(
    page_title="Holiday Home Advisor",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Holiday Home Advisor")

st.write(
    "Explore regions that could be suitable "
    "for a future holiday home."
)

st.divider()

budget = st.slider(
    "Your budget (CHF)",
    min_value=100000,
    max_value=1500000,
    value=500000,
    step=50000
)

altitude = st.slider(
    "Preferred minimum altitude (m)",
    min_value=0,
    max_value=2500,
    value=1000,
    step=100
)

st.write(f"Your budget: CHF {budget:,}")
st.write(f"Preferred altitude: {altitude} m")

st.info(
    "Your recommendations will appear here "
    "once the data integration is ready."
)
