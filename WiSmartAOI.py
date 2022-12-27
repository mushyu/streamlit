import streamlit as st
import pandas as pd
import numpy as np


def web_page_config():
    page_title = "WiSmartAOI System",
    page_icon = "keybaord",
    layout = "centered",


# Cache the dataframe so it's only loaded once
@st.experimental_memo
def load_data():
    return pd.DataFrame(
        {
            "。C": [56, 20, 20, 47],
            "Deploy": ['Y', 'N', 'N', 'Y'],
        }
    )


def set_buttons():
    st.title('MRK700 AOISystem')
    btn_device = st.button('Device')

    col1, col2, col3 = st.columns(3)

    with col1:
        btn_label = st.button(key='label', label='Quick Labeling')

    with col2:
        btn_retrain = st.button(key='retrain', label='Retrain')

    with col3:
        btn_deploy = st.button(key='deploy', label='Deploy')

    device_list = load_data()

    if btn_device:
        st.dataframe(device_list)
    elif btn_label:
        st.write('Start to Quick Labeling...')
    elif btn_retrain:
        st.write('Start to Retrain...')
    elif btn_deploy:
        st.write('Start to Deploy...')


def main():
    web_page_config()
    set_buttons()


if __name__ == "__main__":
    main()
