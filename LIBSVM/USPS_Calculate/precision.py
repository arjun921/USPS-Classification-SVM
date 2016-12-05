with open('GroundTruth.t','r') as gt:
    GroundTruth = [int (i) for i in gt.readlines()] #readlines gives one line at a time.

with open('uspsOutput','r') as op:
    Output = [int (i) for i in op.readlines()]

tp = sum(1 for i,j in zip(GroundTruth,Output) if i==j==1)
