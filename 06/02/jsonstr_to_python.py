import json

from webencodings import PYTHON_NAMES

json_data = '{"name": "Alice", "age": 25, "hobby": ["reading", "music"]}'
python_obj = json.loads(json_data)
print(python_obj)

print(python_obj["age"])
python_obj["age"] = 26
print(python_obj)

json_str = json.dumps(python_obj)
print(json_str)
