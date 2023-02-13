import json

# Load the annotated legal text
with open('processed_data_mvd.json', 'r') as file:
    data = json.load(file)

#hashset of labels
labels = set()
for i in data:
    labels.add(i['labels'])

print(labels)