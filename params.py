import time
import streamlit as st

@st.cache(show_spinner=False, suppress_st_warning=True)  # Avoid redundant API calls for the same image
def main():
    st.set_page_config(layout='wide')

    st.title('Setting Retrain Parameters')

    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'目前進度 {i + 1} %')
        bar.progress(i + 1)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
