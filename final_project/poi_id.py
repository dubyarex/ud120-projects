#! C:/Anaconda3/envs/ud120/python

from pprint import pprint
import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

features_list = ['poi',
                 'salary',
                 'total_payments',
                 'bonus',
                 'total_stock_value',
                 'expenses'] 
### You will need to use more features

# Added: total_payments, bonus, total_stock_value, expenses

# Financial Features: ['salary', 'deferral_payments', 'total_payments',
#                      'loan_advances', 'bonus', 'restricted_stock_deferred',
#                      'deferred_income', 'total_stock_value', 'expenses',
#                      'exercised_stock_options', 'other', 'long_term_incentive',
#                      'restricted_stock', 'director_fees']
#
# Email Features: ['to_messages', 'email_address', 'from_poi_to_this_person',
#                  'from_messages', 'from_this_person_to_poi',
#                   'shared_receipt_with_poi']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

# Remove the Total entry from the dataset -- quirk of the input data
data_dict.pop('TOTAL', 0)


### Task 3: Create new feature(s)

# Helper Functions to create new features
def computeFraction( poi_messages, all_messages ):
	if poi_messages == 'NaN':
		fraction = 0.
	elif poi_messages == 'NaNNaN':
		fraction = 0.
	else:
		fraction = float(poi_messages) / all_messages
	return fraction

for name in data_dict:
	data_point = data_dict[name]

	from_poi_to_this_person = data_point['from_poi_to_this_person']
	to_messages = data_point['to_messages']
	data_point['fraction_from_poi'] = computeFraction(from_poi_to_this_person, to_messages)

	from_this_person_to_poi = data_point['from_this_person_to_poi']
	from_messages = data_point['from_messages']
	data_point['fraction_to_poi'] = computeFraction(from_this_person_to_poi, from_messages)

	total_poi = from_poi_to_this_person + from_this_person_to_poi
	total_messages = to_messages + from_messages
	data_point['fraction_total_poi'] = computeFraction(total_poi, total_messages)


custom_features = ['fraction_from_poi',
                   'fraction_to_poi',
                   'fraction_total_poi']
for cf in custom_features:
	features_list.append(cf)

print
print features_list
print


### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, remove_NaN=True, remove_all_zeroes=True, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

### Example starting point. Try investigating other evaluation techniques!
#  *** cross_validation module was deprecated in version 0.18 in favor of 
#      model_selection  ***
# from sklearn.cross_validation import train_test_split
from sklean.model_selection import train_test_split
 features_train, features_test, labels_train, labels_test = \
     train_test_split(features, labels, test_size=0.3, random_state=42)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)