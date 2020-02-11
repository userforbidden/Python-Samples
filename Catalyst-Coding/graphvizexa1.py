import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

dot = graphviz.Digraph(comment='Example',filename='example')

edges = [[1,2],[7,9],[2,4],[2,5],[3,6],[1,3],[3,7],[4,8]]
edge_level_map = {}
# print(edges.sort)
edges = sorted(edges)
print(edges)
# level = -1
edge_level_map[edges[0][0]] = 0
# print(edge_level_map)
for edge in edges:
    if edge[1] not in edge_level_map.keys():
        edge_level_map[edge[1]] = edge_level_map[edge[0]] + 1
    dot.edge(('PID='+str(edge[0])+'\nLEVEL='+str(edge_level_map[edge[0]])),('PID='+str(edge[1])+'\nLEVEL='+str(edge_level_map[edge[1]])))
dot.view()
# print(dir(dot))
# print(dot._attr_list)
# print(dot.source)