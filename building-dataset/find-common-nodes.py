import json

# Load the annotated legal text
with open('building-dataset/json/processed_data_mvd.json', 'r') as file:
    data = json.load(file)

n = int(input("Enter minimum number of occurences: "))

normalised_names = {}
for i in data:
    if i['normalized_name'] not in normalised_names:
        normalised_names[i['normalized_name']] = {'labels': [i['labels']], 'count': 1, 'document_id': [i['document_id']]}
    else:
        if i['document_id'] not in normalised_names[i['normalized_name']]['document_id']:
            normalised_names[i['normalized_name']]['labels'].append(i['labels'])
            normalised_names[i['normalized_name']]['count'] += 1
            normalised_names[i['normalized_name']]['document_id'].append(i['document_id'])

id_set = set()
for i in normalised_names:
    if normalised_names[i]['count'] > n:
        print(i, normalised_names[i])
        for j in normalised_names[i]['document_id']:
            id_set.add(j)

print(id_set)
#generate MATCH query for the following document_id in id_set
query = "MATCH (n) WHERE n.case_id IN ["
for i in id_set:
    query += str(i) + ", "

query = query[:-2] + "] RETURN n"
print(query)