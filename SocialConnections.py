from collections import defaultdict
friend_nodes = 6
friend_edges = 6
friends_from = [1, 2, 2, 3, 4, 5]
friends_to = [2, 4, 5, 5, 5, 6]

def bestTrio(friend_nodes,friends_from,friends_to):
    graph = defaultdict(list)
    for u,v in zip(friends_from,friends_to):
        graph[u].append(v)
        graph[v].append(u)
    
    print(graph)

bestTrio(friend_nodes,friends_from,friends_to)