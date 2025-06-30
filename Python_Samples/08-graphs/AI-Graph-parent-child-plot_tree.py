import networkx as nx
import plotly.graph_objects as go
import plotly.offline as pyo

# Define the parent-child list
parent_child_list = [
    ("Root", "Child 1", "Parent-Child"),
    ("Root", "Child 2", "Parent-Child"),
    ("Child 1", "Grandchild 1", "Parent-Child"),
    ("Child 2", "Grandchild 2", "Parent-Child"),
    ("Child 1", "Grandchild 3", "Parent-Child"),
    ("Grandchild 1", "Great Grandchild 1", "Parent-Child")
]

# Create a graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for parent, child, label in parent_child_list:
    G.add_node(parent)
    G.add_node(child)
    G.add_edge(parent, child, label=label)

# Position the nodes in a tree-like structure
pos = nx.shell_layout(G)

# Publish the graph to an HTML file
node_x = []
node_y = []
for node in G.nodes():
    node_x.append(pos[node][0])
    node_y.append(pos[node][1])

edge_x = []
edge_y = []
for edge in G.edges():
    source, target = edge
    x0, y0 = pos[source]
    x1, y1 = pos[target]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode='markers+text',
    text=[node for node in G.nodes()],
    textposition='bottom center',
    hoverinfo='text',
    hovertext=[node for node in G.nodes()],
    marker=dict(size=10)
)

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    mode='lines',
    line_shape='spline',
    opacity=0.5,
    hoverinfo='none'
)

edge_labels_x = []
edge_labels_y = []
edge_labels_text = []
for edge in G.edges():
    source, target = edge
    x0, y0 = pos[source]
    x1, y1 = pos[target]
    label_x = (x0 + x1) / 2
    label_y = (y0 + y1) / 2
    edge_labels_x.append(label_x)
    edge_labels_y.append(label_y)
    edge_labels_text.append(G.get_edge_data(source, target)['label'])

edge_label_trace = go.Scatter(
    x=edge_labels_x,
    y=edge_labels_y,
    mode='text',
    text=edge_labels_text,
    textposition='middle center',
    hoverinfo='none'
)

fig = go.Figure(data=[edge_trace, node_trace, edge_label_trace])
fig.update_layout(
    showlegend=False,
    hovermode='x',
    margin=dict(b=20, l=5, r=5, t=40),
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    dragmode='pan'
)

pyo.plot(fig, filename='tree.html', auto_open=True)
