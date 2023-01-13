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
st.text("Experiments: " + this_exp_name)

# 抓取此experiment的所有runs
st.sidebar.text("Experiments: \n   " + this_exp_name)
if st.sidebar.button('Search Runs'):
    with st.spinner('載入資料中，請稍候...'):
        runs = mlflow.search_runs(experiment_names=[this_exp_name])
        run_list = []
        for run in runs:
            run_list = run_list.append(run)

        gb = GridOptionsBuilder.from_dataframe(runs)
        gb.configure_column('run_id', pinned='left')
        gridOptions = gb.build()
        AgGrid(
            runs,
            gridOptions=gridOptions,
            height=200,
            weight=1000
        )
        runs = mlflow.search_runs(
            experiment_names=[this_exp_name],
            output_format="list",
        )

    st.sidebar.selectbox(key='run_list', label="Run name", options=(run_list), disabled=False, index=0)
#         last_run = runs[-1]
#         model_id = last_run.info.run_id
#         st.text(last_run.info.run_id)
#         client = mlflow.tracking.MlflowClient()
#         history = client.get_metric_history(model_id, "loss")
#         st.text(history)
#         value = []
#         step = []
#         for item in history:
#             value.append(item.value)
#             step.append(item.step)
#         st.text(value)
#         st.text(step)
#         options = {

#             "tooltip": {
#                 "trigger": 'item',
#                 "axisPointer": {
#                     "type": 'shadow'
#                 },
#                 "formatter": '{a}｜{c}'
#             },
#             "legend": {
#                 "show": False
#             },

#             "xAxis": {
#                 "type": 'category',
#                 "data": step
#             },
#             "yAxis": {
#                 "type": 'value'
#             },
#             "series": [
#                 {
#                     "data": value,
#                     "type": 'line'
#                 }
#             ]
#         };
#         st_echarts(options=options)

# 選擇runs作為要註冊的模型




# 註冊模型
if st.sidebar.button('Register Model'):
    client.create_registered_model("libby_dog_classfication_train")
    result = client.create_model_version(
        name="libby_dog_classfication_train",
        source="/project/phusers/phapplications/mlflow-507xp/mlruns/3/005aadf7bc954e368d5131087c4ece2e/artifacts/model",
        run_id="005aadf7bc954e368d5131087c4ece2e"
    )

#     result = mlflow.register_model(
#     "runs:/d16076a3ec534311817565e6527539c0/sklearn-model",
#     "sk-learn-random-forest-reg"
#     )


# 刪除已註冊模型
# if st.sidebar.button('delete'):
# Delete versions 1,2, and 3 of the model
#     client = MlflowClient()
#     versions=[1, 2, 3]
#     for version in versions:
#         client.delete_model_version(name="sk-learn-random-forest-reg-model", version=version)

# Delete a registered model along with all its versions
#     client.delete_registered_model(name=this_exp_name)


#
#         history_accuracy=client.get_metric_history(model_id, "accuracy")
#         st.text(history_accuracy)
#         value = []
#         step = []
#         for item in history_accuracy:
#             value.append(item.value)
#             step.append(item.step)
#         st.text(value)
#         st.text(step)
#         options = {

#                 "tooltip": {
#                     "trigger": 'item',
#                     "axisPointer": {
#                         "type": 'shadow'
#                     },
#                     "formatter": '{a}｜{c}'
#                   },
#                   "legend": {
#                       "show": False
#                   },

#                   "xAxis": {
#                     "type": 'category',
#                     "data": step
#                   },
#                   "yAxis": {
#                     "type": 'value'
#                   },
#                   "series": [
#                     {
#                       "data": value,
#                       "type": 'line'
#                     }
#                   ]
#             };
#         st_echarts(options=options)