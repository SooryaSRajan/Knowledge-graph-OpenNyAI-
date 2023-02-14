#load json
import json

f = open('json/cleaned_dataset_mvd_new.json')

# f is an array, filter fields which does not have "doc" field
data = [i for i in json.load(f) if "doc" in i]

for i in data:
    print(i)

#export json
json_object = json.dumps(data, indent=4)
# save to file
with open("json/docs_only_mvd_clean.json", "w") as outfile:
    outfile.write(json_object)
