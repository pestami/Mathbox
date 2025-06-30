import networkx as nx
import matplotlib.pyplot as plt

# Define the tree structure as a parent-child list
tree = [
    {"id": 1, "name": "Root", "parent": None},
    {"id": 2, "name": "Child 1", "parent": 1},
    {"id": 3, "name": "Child 2", "parent": 1},
    {"id": 4, "name": "Grandchild 1", "parent": 2},
    {"id": 5, "name": "Grandchild 2", "parent": 2},
    {"id": 6, "name": "Grandchild 3", "parent": 3},
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for node in tree:
    G.add_node(node["id"], name=node["name"])

# Add edges to the graph
for node in tree:
    if node["parent"] is not None:
        G.add_edge(node["parent"], node["id"])

# Position the nodes in the graph
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")

# Show the plot
plt.show()
