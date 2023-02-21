import json
from opennyai import Pipeline
from opennyai.utils import Data

f = open('building-dataset/json/docs_only_mvd_clean.json')
f = json.load(f)

processed_results = []
pipeline = Pipeline(components=['NER'], use_gpu=True, verbose=True)

print(f[0])

for i in f:

    if i['divtype'] != 'judgments':
        continue

    tid = i['tid']
    doc = i['doc']
    date = i['publishdate']
    title = i['title']
    data = Data([doc])

    try:
        results = pipeline(data)
        results[0]['tid'] = tid
        results[0]['publishdate'] = date
        results[0]['title'] = title

        processed_results.append(results[0])
    except Exception as e:
        print(e)
        continue

json_object = json.dumps(processed_results, indent=4)
with open("json/mvd_annotated_dataset.json", "w") as outfile:
    outfile.write(json_object)