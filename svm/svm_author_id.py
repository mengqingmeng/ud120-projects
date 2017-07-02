#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

from sklearn import svm
clf = svm.SVC(C=10000.0, cache_size=200, class_weight=None, coef0=0.0,
        decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
            max_iter=-1, probability=False, random_state=None, shrinking=True,
                tol=0.001, verbose=False)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
#answer = pred[10] #result=1
#answer = pred[26] #result=0
#print type(pred) #'numpy.ndarray'
#answer = pred[50] #result=1
#print "result=",answer
#print "result=",clf.score(features_test,labels_test)
print "size:", pred.size

sum = 0 
for i in pred:
	if i >0:
		sum = sum +1
print sum


#kernel="rbf",C=10000.0  0.892491467577
#kernel="rbf",C=1000.0  0.821387940842
#kernel="rbf",C=1.0  0.616040955631
#########################################################


