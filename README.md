# symmetrical-adventure
This was our final assignment for Semester 1 Machine Learning.

We were told to Use the usps data set from https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/
and report precision and recall for each class in the data set.

Steps Followed:

1. Download libsvm
2. Read README of libsvm
3. Go to downloaded folder of libsvm via terminal
4. Execute the make commmand for your system.
5. Download USPS dataset
6. usps = Training File
7. usps.t = testing file. usps.t has the outputs for creating ground truth file to check accuracy of classifier.
8. Copy Datasets to libsvm folder.
9. Run command $- svm-train usps //commands may vary according to platform, refer readme of LIBSVM for further clarification. This step will create a model from the training set.
10. Run command $- svm-predict usps.t usps.model output

#####This uses usps.t to run it through usps
#####This gives predictions in a file named output within pwd
####Created for Dr. Asharaf S.
