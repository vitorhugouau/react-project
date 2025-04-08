"""
Exemplo de algoritmo ganancioso - Dijakstra.

Solução do caminho mais curto.
"""

#TODO:1. Definir: representar o grafo(mapa) e a tabela de soluções
DISTANCE = 0
PREDECESSOR = 1
INFINITY = float("inf")


map = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 5,"D":2},
    "C": {"A": 3,"B": 5,"D": 3,"E": 3},
    "D":{"B": 2,"C": 1,"E": 4},
    "E":{"C": 3,"D":4},
}
table = {
    "A":[0, None],
    "B":[INFINITY, None],
    "C":[INFINITY, None],
    "D":[INFINITY, None],
    "E":[INFINITY, None],

}

def get_shortest_distance(table: dict , vertex: str) -> int:
    """
    função que retorna a distancia mais curta de um vertice a partir da origem.
    """
    return table[vertex][DISTANCE]
    ...

def set_shortest_distance(table: dict, vertex: str, distance: int):
    """
    função que atualiza a distancia mais curta na tabela.
    """
    table[vertex][DISTANCE] = distance

def set_predecessor(table: dict, vertex: str,predecessor: str):
    """
    função que atualiza o antecessor na tabela.
    """
    table[vertex][PREDECESSOR] = predecessor

def get_distance(map: dict, first_vertex: str, second_vertex: str):
    """
    função que retorne a distância entre 2 vertices.
    """
    return map[first_vertex][second_vertex]


def get_next_vertex(table:dict, visited: list):
    """
    função que retorna o proximo vertice a ser visitado
    """
    unvisited = list(
        set(
            table.keys()
        ).difference(visited)

    )
    min_vertex = unvisited[0]
    min_distance = table[unvisited[0]][DISTANCE]
    
    for vertex in unvisited:
        if table[vertex][DISTANCE] < min_distance:
            min_vertex = vertex
            min_distance = table[vertex][DISTANCE]

    return min_vertex


def find_shortes_path(map:dict, table:dict,origin: str = "A"):
    """
    função que principal que resolve o problema do caminho mais curto.
    """
    visited = []
    current = origin
    start = origin

    while True:
        adjacent_vertex = map[current]

        if set(adjacent_vertex).issubset(set(visited)):
            ...
            
        unvisted = set(adjacent_vertex).difference(set(visited))

        for vertex in unvisted:
            distance_from_start = get_shortest_distance(table,vertex)
            
            if distance_from_start == INFINITY and current == start:
                total_distance = get_distance(map,vertex,current)
            else:
                total_distance = get_shortest_distance(table,current)
                total_distance += get_distance(map, current, vertex)
        

            if total_distance < distance_from_start:
                set_shortest_distance(table, vertex,total_distance)
                set_predecessor(table, vertex, current)

        visited.append(current)    
            
        if len(visited) == len(table.keys()):
            break

        current = get_next_vertex(table, visited)

    return table



def rota(destino, solucoes):
    rota = []
    atual = destino
    
    while atual is not None:
        rota.append(atual)
        atual = solucoes[atual][1]

    return rota[::-1]

result = find_shortes_path(map, table)
print(result)

gps = rota("D", table)
print(gps)



