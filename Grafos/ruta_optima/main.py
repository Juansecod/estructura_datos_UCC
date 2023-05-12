import matplotlib.pyplot as plt
import networkx as nx
from utils.dijkstra import dijkstra

G = nx.Graph()

cities = ["Bog","Med","Cal","Ara","Car","Nei","Iba","Buc","Rio","J", "Pas"]

edges = (
    (cities[0], cities[1], {'weight': 1.0}),
    (cities[0], cities[2], {'weight': 1.0}),
    (cities[0], cities[3], {'weight': 1.5}),
    (cities[1], cities[2], {'weight': 2.0}),
    (cities[1], cities[3], {'weight': 4.0}),
    (cities[1], cities[4], {'weight': 3.0}),
    (cities[2], cities[5], {'weight': 3.0}),
    (cities[2], cities[5], {'weight': 3.0}),
    (cities[2], cities[6], {'weight': 4.0}),
    (cities[3], cities[4], {'weight': 1.5}),
    (cities[3], cities[5], {'weight': 3.0}),
    (cities[3], cities[7], {'weight': 4.0}),
    (cities[4], cities[5], {'weight': 1.0}),
    (cities[4], cities[7], {'weight': 1.0}),
    (cities[5], cities[7], {'weight': 2.0}),
    (cities[5], cities[6], {'weight': 4.0}),
    (cities[6], cities[8], {'weight': 3.0}),
    (cities[8], cities[9], {'weight': 1.0}),
    (cities[2], cities[10], {'weight': 5.0}),
    (cities[5], cities[10], {'weight': 3.0})
)

G.add_edges_from(edges)
    

print("""
Ciudades disponibles:
    - Bog
    - Med
    - Cal
    - Ara
    - Car
    - Nei
    - Iba
    - Buc
    - Rio
    - J
    - Pas
    
Si quieres finalizar el programa escribe 'salir'
""")

while True:
    start = input("Ingresa tu ciudad de origen: ").capitalize()
    if start.lower() == "salir":
        break
    
    end = input("Ingresa tu ciudad destino: ").capitalize()
    if end.lower() == "salir":
        break
    
    
    result = dijkstra(start, end, G)
    print(f"La ruta optima para ir de {start} a {end} es: {result[0]}")
    print(f"El consumo total es de {result[1]}")

print("Finalizando programa...")
















""" elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
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
plt.show() """ 