import json
from opennyai import Pipeline
from opennyai.utils import Data

f = open('json/docs_only_mvd_clean.json')
f = json.load(f)

processed_results = []
pipeline = Pipeline(components=['NER'], use_gpu=True, verbose=True)

for i in f:
    tid = i['tid']
    doc = i['doc']

    data = Data([doc])

    try:
        results = pipeline(data)
        results[0]['id'] = tid
        processed_results.append(results[0])
    except Exception as e:
        print(e)
        continue

json_object = json.dumps(processed_results, indent=4)
with open("json/dataset_processed.json", "w") as outfile:
    outfile.write(json_object)