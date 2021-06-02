from collections import defaultdict
class Graph: 
    #constructor
    def __init__(self):
        self.graph = defaultdict(list)
    #funcion para adicionar nodos al grafo 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    #funcion para crear el arbol utilizando anchura 
    def BFS(self,s):
        visited = []
        queue = []
        parents = {}
        parents[s] = None

        queue.append(s)
        visited.append(s)

        while queue:
            #print("lista abiertos")
            #print(queue)
            s=queue.pop(0)
            #print(s,end = "")
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    parents[i] = s
        return parents

class Graph2:
    #constructor
    def __init__(self):
        self.graph = defaultdict(list)
    #funcion para adicionar nodos al grafo 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    #funcion para crear el arbol utilizando profundidad
    def BFS(self,s):
        visited = []
        queue = []
        parents = {}
        parents[s] = None

        queue.append(s)
        visited.append(s)

        while queue:
            #print("lista abiertos")
            #print(queue)
            s=queue.pop(0)
            #print(s,end = "")
            for i in self.graph[s]:
                if i not in visited:
                    queue.insert(0,i)
                    visited.append(i)
                    parents[i] = s
        return parents

def pathFormOrign(origin,n,parents):
        if origin == n:
            return[]
        pathO = [n]
        i = n 
        while True:
            i = parents[i]
            pathO.insert(0,i)
            if i == origin:
                return pathO

g = Graph()
g.addEdge('A','C')
g.addEdge('A','B')
g.addEdge('B','A')
g.addEdge('B','D')
g.addEdge('B','E')
g.addEdge('C','A')
g.addEdge('C','F')
g.addEdge('D','B')
g.addEdge('E','F')
g.addEdge('E','B')
g.addEdge('F','C')
g.addEdge('F','E')

g2 = Graph2()
g2.addEdge('A','C')
g2.addEdge('A','B')
g2.addEdge('B','A')
g2.addEdge('B','D')
g2.addEdge('B','E')
g2.addEdge('C','A')
g2.addEdge('C','F')
g2.addEdge('D','B')
g2.addEdge('E','F')
g2.addEdge('E','B')
g2.addEdge('F','C')
g2.addEdge('F','E')

g3 = Graph()

g3.addEdge('A','B')
g3.addEdge('A','D')
g3.addEdge('A','S')
g3.addEdge('B','A')
g3.addEdge('B','C')
g3.addEdge('B','E')
g3.addEdge('C','B')
g3.addEdge('D','A')
g3.addEdge('D','E')
g3.addEdge('D','S')
g3.addEdge('E','B')
g3.addEdge('E','D')
g3.addEdge('E','F')
g3.addEdge('F','E')
g3.addEdge('F','G')
g3.addEdge('G','F')
g3.addEdge('S','A')
g3.addEdge('S','D')



g4 = Graph2()
g4.addEdge('A','B')
g4.addEdge('A','D')
g4.addEdge('A','S')
g4.addEdge('B','A')
g4.addEdge('B','C')
g4.addEdge('B','E')
g4.addEdge('C','B')
g4.addEdge('D','A')
g4.addEdge('D','E')
g4.addEdge('D','S')
g4.addEdge('E','B')
g4.addEdge('E','D')
g4.addEdge('E','F')
g4.addEdge('F','E')
g4.addEdge('F','G')
g4.addEdge('G','F')
g4.addEdge('S','A')
g4.addEdge('S','D')

g5=Graph()
g5.addEdge('Arad','Sibiu')
g5.addEdge('Arad','Timisoara')
g5.addEdge('Arad','Zerind')
g5.addEdge('Bucharest','Giurgiu')
g5.addEdge('Bucharest','Orziceni')
g5.addEdge('Craiova','Dobreta')
g5.addEdge('Craiova','Pitesti')
g5.addEdge('Craiova','Rimnicu Vilcea')
g5.addEdge('Dobreta','Craiova')
g5.addEdge('Dobreta','Mehadia')
g5.addEdge('Fagaras','Bucharest')
g5.addEdge('Fagaras','Sibiu')
g5.addEdge('Giurgiu','Bucharest')
g5.addEdge('Hirsova','Eforie')
g5.addEdge('Hirsova','Orziceni')
g5.addEdge('Lasi','Neamt')
g5.addEdge('Lasi','Vaslui')
g5.addEdge('Lugoj','Mehadia')
g5.addEdge('Lugoj','Timisoara')
g5.addEdge('Mehadia','Dobreta')
g5.addEdge('Mehadia','Lugoj')
g5.addEdge('Neamt','Lasi')
g5.addEdge('Oradea','Sibiu')
g5.addEdge('Oradea','Zerind')
g5.addEdge('Orziceni','Bucharest')
g5.addEdge('Orziceni','Hirsova')
g5.addEdge('Orziceni','Vaslui')
g5.addEdge('Pitesti','Bucharest')
g5.addEdge('Pitesti','Rimnicu Vilcea')
g5.addEdge('Rimnicu Vilcea','Pitesti')
g5.addEdge('Rimnicu Vilcea','Sibiu')
g5.addEdge('Sibiu','Arad')
g5.addEdge('Sibiu','Fagaras')
g5.addEdge('Timisoara','Arad')
g5.addEdge('Timisoara','Lugoj')
g5.addEdge('Vaslui','Lasi')
g5.addEdge('Vaslui','Orziceni')
g5.addEdge('Zerind','Arad')
g5.addEdge('Zerind','Oradea')

g6=Graph2()

g6.addEdge('Arad','Sibiu')
g6.addEdge('Arad','Timisoara')
g6.addEdge('Arad','Zerind')
g6.addEdge('Bucharest','Giurgiu')
g6.addEdge('Bucharest','Orziceni')
g6.addEdge('Craiova','Dobreta')
g6.addEdge('Craiova','Pitesti')
g6.addEdge('Craiova','Rimnicu Vilcea')
g6.addEdge('Dobreta','Craiova')
g6.addEdge('Dobreta','Mehadia')
g6.addEdge('Fagaras','Bucharest')
g6.addEdge('Fagaras','Sibiu')
g6.addEdge('Giurgiu','Bucharest')
g6.addEdge('Hirsova','Eforie')
g6.addEdge('Hirsova','Orziceni')
g6.addEdge('Lasi','Neamt')
g6.addEdge('Lasi','Vaslui')
g6.addEdge('Lugoj','Mehadia')
g6.addEdge('Lugoj','Timisoara')
g6.addEdge('Mehadia','Dobreta')
g6.addEdge('Mehadia','Lugoj')
g6.addEdge('Neamt','Lasi')
g6.addEdge('Oradea','Sibiu')
g6.addEdge('Oradea','Zerind')
g6.addEdge('Orziceni','Bucharest')
g6.addEdge('Orziceni','Hirsova')
g6.addEdge('Orziceni','Vaslui')
g6.addEdge('Pitesti','Bucharest')
g6.addEdge('Pitesti','Rimnicu Vilcea')
g6.addEdge('Rimnicu Vilcea','Pitesti')
g6.addEdge('Rimnicu Vilcea','Sibiu')
g6.addEdge('Sibiu','Arad')
g6.addEdge('Sibiu','Fagaras')
g6.addEdge('Timisoara','Arad')
g6.addEdge('Timisoara','Lugoj')
g6.addEdge('Vaslui','Lasi')
g6.addEdge('Vaslui','Orziceni')
g6.addEdge('Zerind','Arad')
g6.addEdge('Zerind','Oradea')



print('Arbol generado por anchura, busqueda ejercicio visto en clase (origen C busca D)',pathFormOrign('C','D',g.BFS('C'))) 
print('Arbol generado por profundidad, busqueda ejercicio visto en clase (origen C busca D)',pathFormOrign('C','D',g2.BFS('C'))) 
print('Arbol generado por anchura, busqueda ejercicio del deber (origen S busca G)',pathFormOrign('S','G',g3.BFS('S'))) 
print('Arbol generado por profundidad, busqueda ejercicio del deber (origen S busca G)',pathFormOrign('S','G',g4.BFS('S'))) 
print('Arbol generado por profundidad, busqueda ejercicio del deber (origen Arad busca Bucharest)',pathFormOrign('Arad','Bucharest',g6.BFS('Arad'))) 
print('Arbol generado por anchura, busqueda ejercicio del deber (origen Arad busca Bucharest)',pathFormOrign('Arad','Bucharest',g5.BFS('Arad'))) 