#! C:/Anaconda3/envs/ud120/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
import numpy as np
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

print len(features)

### your code goes here 

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

### it's all yours from here forward!  
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
precision = precision_score(pred, labels_test)
recall = recall_score(pred, labels_test)


print "Accuracy: {}".format(accuracy)
print "Precision: {}".format(precision)
print "Recall: {}".format(recall)

true_pos = 0

for i in range(len(pred)):
	if pred[i] == 1 and labels_test[i] ==1:
		true_pos += 1

print true_pos
	
