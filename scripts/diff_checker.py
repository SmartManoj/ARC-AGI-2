import json
import subprocess

cmd = 'git diff main -- data/evaluation/1ae2feb7.json'
output = subprocess.check_output(cmd, shell=True).decode('utf-8')
for line in output.split('\n'):
    if line.startswith('---'):
        continue
    if line.startswith('+++'):
        continue
    if line.startswith('-'):
        old_data = json.loads(line[1:])
    if line.startswith('+'):
        new_data = json.loads(line[1:])

def compare(old, new):
    info = ''
    for i in range(len(old)):
        for j in range(len(old[0])):
            if old[i][j] != new[i][j]:
                info += f"Row {i+1}, Column {j+1} is different; Old: {old[i][j]}, New: {new[i][j]}\n"
    return info

for split in ['train', 'test']:
    no_of_data = len(old_data[split])
    for data_idx in range(no_of_data):
        for key in ['input','output']:
            old = old_data[split][data_idx][key]
            new = new_data[split][data_idx][key]
            info =compare(old, new)
            if info:
                print(split,key, data_idx+1)
                print(info.strip())
                print('---'*25)