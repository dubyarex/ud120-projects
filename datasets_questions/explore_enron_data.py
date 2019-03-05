#! C:/Anaconda3/envs/ud120/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import cPickle, pprint

enron_data = cPickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
num_ppl = len(enron_data)

print "Number of people: {}".format(num_ppl)
print
print enron_data.keys()[0]
pprint.pprint(enron_data[enron_data.keys()[0]])
print
print len(enron_data[enron_data.keys()[0]])

poi = 0
for p in enron_data:
	if enron_data[p]["poi"] == 1:
		poi += 1

print "POIs: {}".format(poi)
print
print "James Prentice Total Stock Value: ", \
	enron_data["PRENTICE JAMES"]["total_stock_value"]
print
print "Wesley Colwell Emails to POIs: ", \
	enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print
print "Jeffery K Skilling's excerised stock options: ", \
	enron_data["SKILLING JEFFREY K"]['exercised_stock_options']


mgmt = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
top_paid = ''
top_pmt = 0
for i in mgmt:
	if enron_data[i]["total_payments"] > top_pmt:
		top_paid = i
		top_pmt = enron_data[i]["total_payments"]

print
print "Top Paid: {} - ${}".format(top_paid, top_pmt)


salaried = 0
known_email = 0

for person in enron_data:
	if enron_data[person]["salary"] != 'NaN':
		salaried += 1

for email in enron_data:
	if enron_data[email]["email_address"] != 'NaN':
		known_email += 1

print
print "salaried: {}".format(salaried)
print "known emails: {}".format(known_email)

no_pay = 0
for person in enron_data:
	if enron_data[person]["total_payments"] == 'NaN':
		no_pay += 1

print no_pay
no_pay_pct = float(no_pay)/num_ppl
print no_pay_pct	

print
print "--------------"
print


no_pay_poi = 0
for person in enron_data:
	if enron_data[person]["total_payments"] == 'NaN' and \
		enron_data[person]["poi"] == 1:
			no_pay_poi += 1

print no_pay_poi
no_pay_poi_pct = float(no_pay_poi)/poi
print no_pay_poi_pct
