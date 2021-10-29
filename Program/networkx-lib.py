import networkx as nx
import matplotlib.pyplot as plt
G=nx.barabasi_albert_graph(50,2)

nx.draw(G)
plt.show()

nx.write_gexf(G,"analysis.gexf")
