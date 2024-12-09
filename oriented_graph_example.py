import networkx as nx
import matplotlib.pyplot as plt
from fontTools.subset import prune_hints

# ---directed graph---
G = nx.DiGraph(directed=True)
num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N'}
# print(value(num_for_letter))

# add nodes
for key, value in num_for_letter.items():
    G.add_node(value)
# G.add_node("San Francisco")
# G.add_node("Tokyo")
# G.add_nodes_from(["Riga", "Copenhagen"])

# add edges

# for i in (len(num_for_letter)):
# for j in range (len(num_for_letter)):
#     print(num_for_letter(j))

for key, value in num_for_letter.items():
    for key1, value1 in num_for_letter.items():
        if value == value1:
            continue
        G.add_edge(value, value1)
# G.add_edge("Singapore", "San Francisco")
# G.add_edge("San Francisco", "Tokyo")
# G.add_edges_from(
#     [
#         ("Riga", "Copenhagen"),
#         ("Copenhagen", "Singapore"),
#         ("Singapore", "Tokyo"),
#         ("Riga", "San Francisco"),
#         ("San Francisco", "Singapore"),
#     ]
# )
# set layout
# pos = nx.circular_layout(G)

options = {
    'node_color': 'white',  # color of node
    'node_size': 500,  # size of node
    'width': 1,  # line width of edges
    'arrowstyle': '-|>',  # array style for directed graph
    'arrowsize': 18,  # size of arrow
    'edge_color': 'blue',  # edge color
}

# draw graph
# nx.draw(G, pos, with_labels = True, arrows=True, **options)

# draw edge labels
# nx.draw_networkx_edge_labels(
#     G, pos,
#     edge_labels={
#         ("Singapore","Tokyo"): '2 flights daily',
#         ("San Francisco","Singapore"): '5 flights daily',
#     },
#     font_color='red'
# )
# nx.draw_planar(G, with_labels=True, arrows=True, **options)
nx.draw_circular(G, with_labels=True, arrows=True, **options)
ax = plt.gca()
ax.collections[0].set_edgecolor("#000000")
plt.show()
