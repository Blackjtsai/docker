import json
import os


file_path = os.path.join(os.getcwd(), '03_webapp', 'backend', 'data.json')
with open(file_path) as f:
    data = json.load(f)
    print(file_path)
    print(data)
