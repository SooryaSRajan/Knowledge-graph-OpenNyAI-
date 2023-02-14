import json

f = open('json/dataset_processed.json')
f = json.load(f)

processed_results = []

for documents in f:
    document_id = documents['id']
    annotations = documents['annotations']

    entities = []
    for annotation in annotations:
        parent_id = annotation['id']
        text = annotation['text']

        for entity in annotation['entities']:
            entity['document_id'] = document_id
            entity['parent_id'] = parent_id
            entity['text'] = text

            labels = entity['labels']

            for label in labels:
                entity['labels'] = label
                entities.append(entity)

    processed_results = processed_results + entities
    print(entities)

json_object = json.dumps(processed_results, indent=4)
with open("json/combined_annotated_data_mvd.json", "w") as outfile:
    outfile.write(json_object)
