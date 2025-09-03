import json
from pyperclip import copy

path = r"data\evaluation\7ed72f31.json"
data = json.load(open(path))

data['test'][1]['input'][21][4] = 2
data['test'][1]['output'][21][4] = 2
with open(path, "w") as f:
    f.write(json.dumps(data))
