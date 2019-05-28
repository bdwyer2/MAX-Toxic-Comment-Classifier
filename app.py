from maxfw.core import MAXApp
from api import ModelMetadataAPI, ModelPredictAPI, ModelLabelsAPI
from config import API_TITLE, API_DESC, API_VERSION

max = MAXApp(API_TITLE, API_DESC, API_VERSION)
max.add_api(ModelMetadataAPI, '/metadata')
max.add_api(ModelPredictAPI, '/predict')
max.add_api(ModelLabelsAPI, '/labels')
max.run()
