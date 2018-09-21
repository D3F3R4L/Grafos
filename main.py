import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import networkx as nx

# Nós

cidades=['Belem','Ananideua','Marituba','Benevides','SantaIzabel','Vigia','Barcarena','Mosqueiro'];

# Arestas

G = nx.Graph()
G.add_edge(cidades[0], cidades[1], weight=50)
G.add_edge(cidades[1], cidades[2], weight=100)
G.add_edge(cidades[0], cidades[6], weight=100)
G.add_edge(cidades[1], cidades[6], weight=220)
G.add_edge(cidades[0], cidades[7], weight=120)
G.add_edge(cidades[1], cidades[7], weight=100)
G.add_edge(cidades[2], cidades[3], weight=80)
G.add_edge(cidades[3], cidades[4], weight=70)
G.add_edge(cidades[4], cidades[5], weight=60)
G.add_edge(cidades[3], cidades[7], weight=140)
G.add_edge(cidades[5], cidades[7], weight=330)

# Calculo do menor caminho
for i in range(len(cidades)):
  print(i, cidades[i])
Partida = int(input('Digite o numero do local de partida:'))
Chegada = int(input('Digite o numero do local de chegada:'))
Distancia,Caminho=nx.single_source_dijkstra(G, cidades[Partida], cidades[Chegada], weight='weight')
print('Percurso:'+'\n',Caminho,'\n'+'Distancia total: ', Distancia)
print('Nós:'+'\n', G.nodes(),'\n'+'Total de Nós: ',len(G.nodes()))
print('Arestas:'+'\n',G.edges(),'\n'+'Total de arestas: ',len(G.edges()))

# print
path=[]
i=0
while i<len(Caminho)-1:
  path.append((Caminho[i],Caminho[i+1]))
  i+=1
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1000)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edges(G, pos, edgelist=path,width=6, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
plt.axis('off')
plt.title('Mapa')
plt.savefig("Mapa.png") 
plt.show() 