import json
from pyperclip import copy

path = r"data\evaluation\e12f9a14.json"
data = json.load(open(path))
# INFO: main.py:70 - At row =4, col = 12, expected_value = 4 != actual_value = 0
# INFO: main.py:70 - At row =8, col = 16, expected_value = 0 != actual_value = 4
# data['test'][1]['input'][21][4] = 2
split = 'train'
idx = 2
for row in range(13,19):
    data[split][idx]['output'][row][row+1] = 4
with open(path, "w") as f:
    f.write(json.dumps(data))
