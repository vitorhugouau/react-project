"""
Representação do mapa da Romênia, junto com a heuristica - distancia em linha reta
do vértice até Bacareste.
"""

class Vertex:
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for adjacent in self.adjacent:
            print(f'Adjacente: {adjacent.vertex.label}- {adjacent.cost} km')
            
class Adjacent:
    def __init__(self,vertex,cost):
        self.vertex = vertex
        self.cost = cost
        
        self.star_distance = vertex.target_distance + cost

class Romania:
    arad = Vertex("Porto Uniãio", 203)
    zerind = Vertex("Paulo Frontin", 172)
    oradea = Vertex("Canoinhas", 141)
    sibiu = Vertex("Três Barras", 131)
    timisoara = Vertex("São Mateus do Sul", 123)
    lugoj = Vertex("irati", 139)
    mehadia = Vertex("Curitiba",0)
    dobreta = Vertex("Palmeira", 59)
    craiova = Vertex("mafra", 94)
    rimnicu = Vertex("Campo Largo", 27)
    fagaras = Vertex("Balsa Nova", 41)
    pitesti = Vertex("Lapa",74)
    giurgiu = Vertex("Tijucas do Sul",56)
    bucarest = Vertex("Araucária",23)
    bucarest = Vertex("São José dos Pinhais",13)
    bucarest = Vertex("Contenda",39)

    arad.add_adjacent(Adjacent(zerind,75))
    arad.add_adjacent(Adjacent(timisoara,118))
    arad.add_adjacent(Adjacent(sibiu,140))

    zerind.add_adjacent(Adjacent(oradea,71))
    zerind.add_adjacent(Adjacent(arad,75))

    oradea.add_adjacent(Adjacent(zerind,71))
    oradea.add_adjacent(Adjacent(sibiu,151))

    sibiu.add_adjacent(Adjacent(rimnicu,80))
    sibiu.add_adjacent(Adjacent(fagaras,99))
    sibiu.add_adjacent(Adjacent(arad, 40))
    sibiu.add_adjacent(Adjacent(oradea, 158))

    timisoara.add_adjacent(Adjacent(lugoj,111))
    timisoara.add_adjacent(Adjacent(arad,118))

    rimnicu.add_adjacent(Adjacent(craiova,146))
    rimnicu.add_adjacent(Adjacent(sibiu,80))
    rimnicu.add_adjacent(Adjacent(pitesti,97))

    fagaras.add_adjacent(Adjacent(sibiu,99))
    fagaras.add_adjacent(Adjacent(bucarest,211))

    lugoj.add_adjacent(Adjacent(mehadia,70))
    lugoj.add_adjacent(Adjacent(timisoara,111))

    mehadia.add_adjacent(Adjacent(lugoj,70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova,120))

    craiova.add_adjacent(Adjacent(dobreta,120))
    craiova.add_adjacent(Adjacent(pitesti,138)) 
    craiova.add_adjacent(Adjacent(rimnicu,146))

    pitesti.add_adjacent(Adjacent(craiova,138))
    pitesti.add_adjacent(Adjacent(rimnicu,97))
    pitesti.add_adjacent(Adjacent(bucarest,101))

    bucarest.add_adjacent(Adjacent(pitesti,101))
    bucarest.add_adjacent(Adjacent(giurgiu,90))
    bucarest.add_adjacent(Adjacent(fagaras,211))