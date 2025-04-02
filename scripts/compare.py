import json
file = '../ARC-AGI-2.worktrees/main/data/training/b74ca5d1.json'
old_data = json.load(open(file, 'r'))
new_file = 'data/training/b74ca5d1.json'
new_data = json.load(open(new_file, 'r'))
def compare(old, new):
    info = ''
    for i in range(len(old)):
        for j in range(len(old[0])):
            if old[i][j] != new[i][j]:
                info += f"Cell {i}, {j} is different; {old[i][j] = } {new[i][j] = }\n"
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