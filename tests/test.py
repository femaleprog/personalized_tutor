import os
import json

data_path = os.path.join(os.path.dirname(__file__),'../data/ai_resources.json')

with open(data_path, 'r') as f:
    resources = json.load(f)
