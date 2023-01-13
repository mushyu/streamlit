import mlflow

tracking_uri = "http://app-mlflow-507xp:5000/"
mlflow.set_tracking_uri(tracking_uri)
print("Current tracking uri: {}".format(tracking_uri))

