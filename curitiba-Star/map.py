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
            print(f"Adjacente: {adjacent.vertex.label} - {adjacent.cost} Km")
            
        
class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        #NEW
        self.star_distance = vertex.target_distance + cost


class Curitiba:
    porto_uniao = Vertex("Porto União", 400)
    paulo_frontin = Vertex("Paulo Frontin", 380)
    irati = Vertex("Irati", 320)
    palmeira = Vertex("Palmeira", 300)
    campo_largo = Vertex("Campo Largo", 100)
    curitiba = Vertex("Curitiba", 0)
    são_josé = Vertex("São José dos Pinhais", 15)
    contenda = Vertex("Contenda", 110)
    balsa_nova = Vertex("Balsa Nova", 80)
    araucária = Vertex("Araucária", 50)
    lapa = Vertex("Lapa", 130)
    são_mateus = Vertex("São Mateus", 350)
    três_barras = Vertex("Três Barras", 370)
    canoinhas = Vertex("Canoinhas", 390)
    mafra = Vertex("Mafra", 180)
    tijucas = Vertex("Tijucas do Sul", 70)

    # Conexões
    porto_uniao.add_adjacent(Adjacent(paulo_frontin, 46))
    porto_uniao.add_adjacent(Adjacent(são_mateus, 87))
    porto_uniao.add_adjacent(Adjacent(canoinhas, 78))

    paulo_frontin.add_adjacent(Adjacent(porto_uniao, 46))
    paulo_frontin.add_adjacent(Adjacent(irati, 75))

    irati.add_adjacent(Adjacent(paulo_frontin, 75))
    irati.add_adjacent(Adjacent(palmeira, 75))
    irati.add_adjacent(Adjacent(são_mateus, 57))

    palmeira.add_adjacent(Adjacent(irati, 75))
    palmeira.add_adjacent(Adjacent(são_mateus, 77))
    palmeira.add_adjacent(Adjacent(campo_largo, 55))

    campo_largo.add_adjacent(Adjacent(palmeira, 55))
    campo_largo.add_adjacent(Adjacent(balsa_nova, 22))
    campo_largo.add_adjacent(Adjacent(curitiba, 29))

    curitiba.add_adjacent(Adjacent(campo_largo, 29))
    curitiba.add_adjacent(Adjacent(araucária, 37))
    curitiba.add_adjacent(Adjacent(são_josé, 15))
    curitiba.add_adjacent(Adjacent(balsa_nova, 51))

    são_josé.add_adjacent(Adjacent(curitiba, 15))
    são_josé.add_adjacent(Adjacent(tijucas, 49))

    tijucas.add_adjacent(Adjacent(são_josé, 49))
    tijucas.add_adjacent(Adjacent(mafra, 99))

    araucária.add_adjacent(Adjacent(curitiba, 37))
    araucária.add_adjacent(Adjacent(contenda, 18))

    balsa_nova.add_adjacent(Adjacent(campo_largo, 22))
    balsa_nova.add_adjacent(Adjacent(contenda, 19))
    balsa_nova.add_adjacent(Adjacent(curitiba, 51))

    contenda.add_adjacent(Adjacent(balsa_nova, 19))
    contenda.add_adjacent(Adjacent(araucária, 18))
    contenda.add_adjacent(Adjacent(lapa, 26))

    lapa.add_adjacent(Adjacent(contenda, 26))
    lapa.add_adjacent(Adjacent(mafra, 57))
    lapa.add_adjacent(Adjacent(são_mateus, 60))

    são_mateus.add_adjacent(Adjacent(lapa, 60))
    são_mateus.add_adjacent(Adjacent(três_barras, 43))
    são_mateus.add_adjacent(Adjacent(porto_uniao, 87))
    são_mateus.add_adjacent(Adjacent(palmeira, 77))
    são_mateus.add_adjacent(Adjacent(irati, 57))

    três_barras.add_adjacent(Adjacent(são_mateus, 43))
    três_barras.add_adjacent(Adjacent(canoinhas, 12))

    canoinhas.add_adjacent(Adjacent(três_barras, 12))
    canoinhas.add_adjacent(Adjacent(mafra, 66))
    canoinhas.add_adjacent(Adjacent(porto_uniao, 78))

    mafra.add_adjacent(Adjacent(canoinhas, 66))
    mafra.add_adjacent(Adjacent(lapa, 57))
    mafra.add_adjacent(Adjacent(tijucas, 99))