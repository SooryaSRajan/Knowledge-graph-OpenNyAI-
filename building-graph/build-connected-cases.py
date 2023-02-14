import json
from neo4j import GraphDatabase
import pandas as pd
import networkx as nx

with open('../building-dataset/json/processed_data_mvd.json', 'r') as file:
    data = json.load(file)

driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "password"))

with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")

df = pd.DataFrame(data)

print(df.columns)

grouped = df.groupby('document_id')

relationShipToCase = {'ORG': 'ORGANIZATION INVOLVED IN CASE',
                      'JUDGE': 'JUDGE OF CASE',
                      'WITNESS': 'WITNESS APPEALED IN CASE',
                      'LAWYER': 'LAWYER IN CAsE',
                      'GPE': 'GPE OF CASE',
                      'PRECEDENT': 'PRECEDENT OF CASE',
                      'RESPONDENT': 'RESPONDENT OF CASE',
                      'CASE_NUMBER': 'CASE NUMBER',
                      'PETITIONER': 'PETITIONER OF CASE',
                      'COURT': 'OF THIS CASE',
                      'OTHER_PERSON': 'OTHER PERSON INVOLVED',
                      'DATE': 'DATE OF TRIAL',
                      'PROVISION': 'PROVISION OF CASE',
                      'STATUTE': 'STATUTE OF CASE'
                      }

count = 0
for name, group in grouped:

    group = group.sample(frac=1)

    G = nx.Graph()
    print(count)
    count = count + 1

    for index, row in group.iterrows():
        G.add_node(row['normalized_name'], type=row['labels'])

    with driver.session() as session:
        caseName = group.iloc[0]['title']
        caseId = group.iloc[0]['document_id']
        session.run("CREATE (n:Node {name: $name, type: $type, case_id: $case_id})", name=caseName, type='CASE',
                    case_id=caseId)

        for node in G.nodes:
            label = G.nodes[node]['type']
            caseId = group.iloc[0]['document_id']
            session.run("CREATE (n:Node {name: $name, type: $type, case_id: $case_id})", name=node,
                        type=label, case_id=caseId)

            relationship = relationShipToCase[label]
            if relationship is None:
                relationship = "IS IN"

            session.run("MATCH (a:Node),(b:Node) WHERE a.name = $from_node AND b.name = $to_node AND b.case_id = "
                        "$case_id AND b.type = 'CASE' "
                        " CREATE (a)-[ "
                        "r:RELATIONSHIP {relationship: $relationship}]->(b)", from_node=node, to_node=caseName,
                        case_id=caseId,
                        relationship=relationship)
