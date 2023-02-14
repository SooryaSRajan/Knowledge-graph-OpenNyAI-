import networkx as nx
import neo4j
import json

# Connect to neo4j graph database
driver = neo4j.GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

print("Neo4j connection status: ", driver.verify_connectivity())

# clear database
with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")
    print("Database cleared")

# Read the annotated dataset
with open('../building-dataset/json/processed_data_mvd.json', 'r') as f:
    data = json.load(f)
    print("Data loaded")

# Create a networkx graph
G = nx.Graph()
print("Networkx graph created")

# Add nodes to the graph
for item in data:
    G.add_node(item['normalized_name'], label=item['labels'])
print("Nodes added to graph")

# Define the relationships based on the labels
relationships = {
    'OTHER_PERSON': 'IS_OTHER_PERSON',
    'PETITIONER': 'IS_PETITIONER',
    'GPE': 'IS_GPE',
    'ORG': 'IS_ORG',
    'WITNESS': 'IS_WITNESS',
    'LAWYER': 'IS_LAWYER',
    'COURT': 'IS_COURT',
    'RESPONDENT': 'IS_RESPONDENT',
    'JUDGE': 'IS_JUDGE',
    'DATE': 'IS_DATE',
    'PRECEDENT': 'IS_PRECEDENT',
    'PROVISION': 'IS_PROVISION',
    'STATUTE': 'IS_STATUTE',
    'CASE_NUMBER': 'IS_CASE_NUMBER'
}

# Add relationships to the graph
for item1 in data:
    for item2 in data:
        if item1['normalized_name'] != item2['normalized_name']:
            if item1['labels'] in relationships and item2['labels'] in relationships:
                G.add_edge(item1['normalized_name'], item2['normalized_name'],
                           relationship=relationships[item1['labels']] + '-' + relationships[item2['labels']])

print("Relationships added to graph")

# Create the nodes and relationships in neo4j
with driver.session() as session:
    for node in G.nodes(data=True):
        session.run("CREATE (n:Node {name: $name, label: $label})", name=node[0], label=node[1]['label'])
    print("Nodes added to neo4j")

with driver.session() as session:
    for edge in G.edges(data=True):
        # print progress indicator to console with percentage but in same line, erase previous value and replace with new
        session.run("MATCH (a:Node),(b:Node) WHERE a.name = $from_node AND b.name = $to_node CREATE (a)-["
                    "r:RELATIONSHIP {relationship: $relationship}]->(b)", from_node=edge[0], to_node=edge[1],
                    relationship=edge[2]['relationship'])
    print("Relationships added to neo4j")

print("Done")

driver.close()
print("Neo4j connection closed")
