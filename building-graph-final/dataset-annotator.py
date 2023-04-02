import json
from opennyai import Pipeline
from opennyai.utils import Data

f = open('data.json')
f = json.load(f)

data = []

for i in f:
    if i['text'] != '':
        data.append(i)

documents = []

processed_results = []
pipeline = Pipeline(components=['NER'], use_gpu=True, verbose=True)

# for i in data:
#     documents.append(i['text'])
#
# data = Data(documents)
# processed_results = pipeline(data)
#
# for i in range(len(processed_results)):
#     processed_results[i]['id'] = data[i]['id']
#     processed_results[i]['title'] = data[i]['title']
#     processed_results[i]['text'] = data[i]['text']
#
#
# json_object = json.dumps(processed_results, indent=4)
# with open("annotated-data.json", "w") as outfile:
#     outfile.write(json_object)


total = len(f)

for i in f:

    tid = i['id']
    doc = i['text']
    title = i['title']

    try:
        data = Data([doc])
        results = pipeline(data)
        results[0]['tid'] = tid
        results[0]['title'] = title

        processed_results.append(results[0])
    except Exception as e:
        print(e)
        continue

json_object = json.dumps(processed_results, indent=4)
with open("annotated-data.json", "w") as outfile:
    outfile.write(json_object)
