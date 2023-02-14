import json
import networkx as nx
from neo4j import GraphDatabase

# Load the annotated legal text
with open('../building-dataset/json/processed_data_mvd.json', 'r') as file:
    data = json.load(file)

#shuffle data
import random
random.shuffle(data)

# Create a dictionary of nodes and their relationships
nodes = {}
for item in data:
    subtext = item['normalized_name']
    label = item['labels']

    if subtext not in nodes:
        nodes[subtext] = {'type': label}

# Create a NetworkX graph
G = nx.Graph()

# Add nodes to the graph
for node in nodes:
    G.add_node(node, type=nodes[node]['type'])

# Add edges to the graph to represent relationships between nodes
# for i in range(len(data) - 1):
#     current = data[i]['normalized_name']
#     next_node = data[i + 1]['normalized_name']
#     #add relationship label
#     relationship = data[i]['labels'] + '-' + data[i + 1]['labels']
#     G.add_edge(current, next_node, relationship=relationship)

# Connect to a neo4j database
driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "password"))

#clear database
with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")

# Create the nodes in the neo4j database
with driver.session() as session:
    for node in nodes:
        session.run("CREATE (n:Node {name: $name, type: $type})", name=node, type=nodes[node]['type'])

# Create the relationships between nodes in the neo4j database
# with driver.session() as session:
#     for edge in G.edges:
#         session.run("MATCH (a:Node),(b:Node) WHERE a.name = $from_node AND b.name = $to_node CREATE (a)-["
#                     "r:RELATIONSHIP {relationship: $relationship}]->(b)", from_node=edge[0], to_node=edge[1],
#                     relationship=G.edges[edge]['relationship'])
#join all nodes based on some common relationship between them
#match (n:Node)-[r:RELATIONSHIP]->(m:Node) where r.relationship = 'IS_GPE-IS_GPE' return n,m
