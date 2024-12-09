import random

import networkx as nx
import matplotlib.pyplot as plt

# ---directed graph---
G = nx.DiGraph(directed=True)
# num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H', 7: 'G', 8: 'K', 9: 'M', 10: 'N'}
num_for_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'H'}
# print(value(num_for_letter))

# add nodes
for key, value in num_for_letter.items():
    G.add_node(value)

i = 0
for key, value in num_for_letter.items():
    for key1, value1 in num_for_letter.items():
        # print (key, key1)
        if value == value1:
            continue
        if i < key1:
            print(key, key1)
            break
        if random.random()>0.8:
            break
        G.add_edge(value, value1)
    i += 1

options = {
    'node_color': 'white',  # color of node
    'node_size': 500,  # size of node
    'width': 1,  # line width of edges
    'arrowstyle': '-|>',  # array style for directed graph
    'arrowsize': 18,  # size of arrow
    'edge_color': 'blue',  # edge color
}

# nx.draw_planar(G, with_labels=True, arrows=True, **options)
nx.draw_circular(G, with_labels=True, arrows=True, **options)
ax = plt.gca()
ax.collections[0].set_edgecolor("#000000")
plt.show()
