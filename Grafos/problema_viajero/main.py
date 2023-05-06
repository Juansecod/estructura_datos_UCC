import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

cities = {
    1: "Bog",
    2: "Med",
    3: "Cal",
    4: "Ara",
    5: "Car",
    6: "Nei",
    7: "Iba",
    8: "Buc",
    9: "Rio",
    10: "J",
    11: "Pas"
}

edges = (
    (cities[1], cities[2], {'weight': 1.0}),
    (cities[1], cities[3], {'weight': 1.0}),
    (cities[1], cities[4], {'weight': 1.5}),
    (cities[2], cities[3], {'weight': 2.0}),
    (cities[2], cities[4], {'weight': 4.0}),
    (cities[2], cities[5], {'weight': 3.0}),
    (cities[3], cities[4], {'weight': 3.0}),
    (cities[3], cities[6], {'weight': 3.0}),
    (cities[3], cities[7], {'weight': 4.0}),
    (cities[4], cities[5], {'weight': 1.5}),
    (cities[4], cities[6], {'weight': 3.0}),
    (cities[4], cities[8], {'weight': 4.0}),
    (cities[5], cities[6], {'weight': 1.0}),
    (cities[5], cities[8], {'weight': 1.0}),
    (cities[6], cities[8], {'weight': 2.0}),
    (cities[6], cities[7], {'weight': 4.0}),
    (cities[7], cities[9], {'weight': 3.0}),
    (cities[9], cities[10], {'weight': 1.0}),
    (cities[3], cities[11], {'weight': 5.0}),
    (cities[6], cities[11], {'weight': 3.0})
)

G.add_edges_from(edges)



elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=2500)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.rcParams['figure.figsize'] = [20, 15]

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()