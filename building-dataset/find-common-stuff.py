import json

# Load the annotated legal text
with open('json/processed_data_mvd.json', 'r') as file:
    data = json.load(file)

#check how many normalised_names are the same between different objects

#map of normalised_names to a list of labels and count of repetitions and do not append if ID -> document_id is the same
#add if condition to check if ID is the same for the same normalised_name, the id in data is called document_id
normalised_names = {}
for i in data:
    #ignore document_id you idiot
    if i['normalized_name'] not in normalised_names:
        normalised_names[i['normalized_name']] = {'labels': [i['labels']], 'count': 1, 'document_id': [i['document_id']]}
    else:
        if i['document_id'] not in normalised_names[i['normalized_name']]['document_id']:
            normalised_names[i['normalized_name']]['labels'].append(i['labels'])
            normalised_names[i['normalized_name']]['count'] += 1
            normalised_names[i['normalized_name']]['document_id'].append(i['document_id'])

for i in normalised_names:
    if normalised_names[i]['count'] > 1:
        print(i, normalised_names[i])