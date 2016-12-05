# symmetrical-adventure
This was our final assignment for Semester 1 Machine Learning.

We were told to Use the usps data set from https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/
and report precision and recall for each class in the data set.

USPS_DATASET/TrainUSPS = Training File
USPS_DATASET/Test = testing file. Also contains outputs for creating ground truth file to check accuracy of classifier.

Steps Followed:

1. Download libsvm
2. Read README of libsvm
3. Go to downloaded folder of libsvm via terminal
4. Execute the make commmand for your system.
5. Download USPS dataset
6. Copy Datasets to libsvm folder.
7. > ./svm-train USPS_DATASET/TrainUSPS
8. > ./svm-predict USPS_DATASET/Test TrainUSPS.model USPS_DATASET/OutputValue

#####This uses usps.t to run it through usps
#####This gives predictions in a file named output within pwd
####Created for Dr. Asharaf S.
