eval1 = r'../ARC-AGI/data/evaluation.txt'
train1 = r'../ARC-AGI/data/training.txt'

eval2 = r'../ARC-AGI-2/data/evaluation.txt'
train2 = r'../ARC-AGI-2/data/training.txt'

# read the contents into set
# first list then set
eval1_list = open(eval1, 'r').read().splitlines()
train1_list = open(train1, 'r').read().splitlines()
eval2_list = open(eval2, 'r').read().splitlines()
train2_list = open(train2, 'r').read().splitlines()

eval1_set = set(eval1_list)
train1_set = set(train1_list)
eval2_set = set(eval2_list)
train2_set = set(train2_list)

arc_agi_set = eval1_set.union(train1_set)
arc_agi_2_set = eval2_set.union(train2_set)

# find the difference between the two sets
# check intersection
diff_set = eval2_set.intersection(eval1_set)
print('Common in eval1 and eval2: ', len(diff_set))
print('Common in eval1 and eval2: ', (diff_set))
# show its index in eval2
idxeval2 = [eval2_list.index(item)+1 for item in diff_set]
print(sorted(idxeval2))
diff_set = train2_set.intersection(train1_set)
print('Common in train1 and train2: ', len(diff_set))
diff_set = train2_set.intersection(eval1_set)
print('Common in train2 and eval2: ', len(diff_set))
diff_set = train2_set.intersection(arc_agi_set)
print('Common in train2 and ARC-AGI: ', len(diff_set))
diff_set = arc_agi_2_set.intersection(arc_agi_set)
print('Common in ARC-AGI and ARC-AGI-2: ', len(diff_set))
