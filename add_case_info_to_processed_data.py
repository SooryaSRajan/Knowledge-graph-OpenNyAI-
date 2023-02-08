import json

dataset = open('combined_annotated_data_mvd.json')
dataset = json.load(dataset)

processed_results = []

case_data = open('docs_only_mvd_clean.json')
case_data = json.load(case_data)

#get publishdate, title and docsource from the case_data for document_id of combined_annotated_data_mvd.json matching id in case_data

# if i['document_id'] == j['id']:
#     i['publishdate'] = j['publishdate']
#     i['title'] = j['title']
#     i['docsource'] = j['docsource']

# create map using tid and data from case_data
mapCaseData = {}
for j in case_data:
    mapCaseData[j['tid']] = j

for i in dataset:
    if i['document_id'] in mapCaseData:
        i['publishdate'] = mapCaseData[i['document_id']]['publishdate']
        i['title'] = mapCaseData[i['document_id']]['title']
        i['docsource'] = mapCaseData[i['document_id']]['docsource']
        processed_results.append(i)

print(processed_results)

json_object = json.dumps(processed_results, indent=4)
# write to file
with open("processed_data_mvd.json", "w") as outfile:
    outfile.write(json_object)