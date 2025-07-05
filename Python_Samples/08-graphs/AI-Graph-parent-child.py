import networkx as nx
import matplotlib.pyplot as plt

# Define the parent-child list
parent_child_list = [
    ("Root", "Child 1"),
    ("Root", "Child 2"),
    ("Child 1", "Grandchild 1"),
    ("Child 2", "Grandchild 2"),
    ("Child 1", "Grandchild 3"),
    ("Grandchild 1", "Great Grandchild 1")
]

# Create a graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for parent, child in parent_child_list:
    G.add_node(parent)
    G.add_node(child)
    G.add_edge(parent, child)

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
