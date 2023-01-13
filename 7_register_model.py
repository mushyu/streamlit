import streamlit as st
from primehub import PrimeHub, PrimeHubConfig
import os
import json
import mlflow
from mlflow.tracking import MlflowClient
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from streamlit_echarts import st_echarts, JsCode

mlflow.set_tracking_uri("http://app-mlflow-507xp:5000/")
client = MlflowClient()
this_exp_name = "libby_dog_classfication_train"

# 抓取此experiment的所有runs
st.sidebar.text("Experiments: \n   " + this_exp_name)
# if st.sidebar.button('Search Runs'):
runs = mlflow.search_runs(experiment_names=[this_exp_name])
st.write('Runs in experiments: ' + this_exp_name)

run_id_list = []
for run_id in runs['run_id']:
    run_id_list.append(run_id)

with st.spinner('載入資料中，請稍候...'):
    gb = GridOptionsBuilder.from_dataframe(runs)

    #         顯示表格(所有欄位)
    #     gb.configure_column('run_id', header_name='Run', pinned='left')
    runs = mlflow.search_runs(
        experiment_names=[this_exp_name],
        output_format="list",
        filter_string="attributes.status = 'FINISHED'")
    st.text(runs)

    gridOptions = gb.build()

    #         顯示表格(部分欄位)
    #     gridOptions["columnDefs"]= [
    #         { "field": 'run_id' },
    #         { "field": 'metrics.accuracy' },
    #         { "field": 'metrics.loss' },
    #         { "field": 'metrics.lr' },
    #         { "field": 'end_time' },
    #         { "field": 'status' }
    #     ]

    AgGrid(
        runs,
        gridOptions=gridOptions, height=200, weight=1200
    )
    runs = mlflow.search_runs(
        experiment_names=[this_exp_name],
        output_format="list",
    )

# 下拉選單: 選擇要註冊的模型id
selected_run_id = st.sidebar.selectbox(key='run_list', label="Select Run: ", options=(run_id_list), disabled=False,
                                       index=0)
st.write("you select: " + selected_run_id)

# 註冊模型
if st.sidebar.button('Register Model'):
    registered_model_name = "dog_classification_model_2"
    runs_uri = "runs:/{}/artifacts/model".format(selected_run_id)

    result = mlflow.register_model(
        runs_uri,
        registered_model_name
    )

    if result is not None:
        st.write("Registration is successful!")
        st.write("Registed Model Name: {}".format(result.name))
        st.write("Registed Model Version: Version {}".format(result.version))
    else:
        st.write("Registration is Faild!")

# 刪除已註冊模型
# if st.sidebar.button('delete'):
# Delete versions 1,2, and 3 of the model
#     client = MlflowClient()
#     versions=[1, 2, 3]
#     for version in versions:
#         client.delete_model_version(name="sk-learn-random-forest-reg-model", version=version)

# Delete a registered model along with all its versions
#     client.delete_registered_model(name=this_exp_name)
