with open('GroundTruth.t','r') as gt:
    GroundTruth = [int (i) for i in gt.readlines()] #readlines gives one line at a time.

with open('uspsOutput','r') as op:
    Output = [int (i) for i in op.readlines()]

def prec_recall(GroundTruth,uspsOutput):
    tp = sum(1 for i, j in zip(GroundTruth, uspsOutput) if i == j == 1)
    precision = tp / GroundTruth.count(1)
    fn = sum(1 for i, j in zip(GroundTruth, uspsOutput) if (i == 1) and (j != 1))
    recall = tp / (tp + fn)
    return precision, recall

print('{} instances in files. {} unique labels'.format(len(GroundTruth), len(set(GroundTruth))))


for label in set(GroundTruth):
    # A one-vs-all scheme
    new_GroundTruth = [(1 if i == label else -1) for i in GroundTruth]
    new_Output = [(1 if i == label else -1) for i in Output]
    # calculate precision recall
    precision, recall = prec_recall(new_GroundTruth, new_Output)
    print("Label {}: Precision {}, Recall {}".format(label, precision, recall))
