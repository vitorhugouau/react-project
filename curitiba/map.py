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


class Curitiba:
    portoUniao = Vertex("Porto União", 203)
    pauloFrontin = Vertex("Paulo Frontin", 172)
    canoinhas = Vertex("Canoinhas", 141)
    tresBarras = Vertex("Três Barras", 131)
    saoMateusDoSul = Vertex("São Mateus do Sul",123)
    irati = Vertex("Irati", 139)
    curitiba = Vertex("Curitiba", 0)
    palmeira = Vertex("Palmeira", 59)
    mafra = Vertex("Mafra", 94)
    campoLargo = Vertex("Campo Largo", 27)
    balsaNova = Vertex("Balsa Nova", 41)
    lapa = Vertex("Lapa", 74)
    tijucasDoSul = Vertex("Tijucas do Sul", 56)
    araucaria = Vertex("Araucária", 23)
    saoJoseDosPinhais = Vertex("São José dos Pinhais", 13)
    contenda = Vertex("Contenda", 39)

    portoUniao.add_adjacent(Adjacent(pauloFrontin, 46))         
    portoUniao.add_adjacent(Adjacent(saoMateusDoSul, 87))
    portoUniao.add_adjacent(Adjacent(canoinhas, 78))  

    pauloFrontin.add_adjacent(Adjacent(irati, 75))        
    pauloFrontin.add_adjacent(Adjacent(portoUniao, 46))   

    canoinhas.add_adjacent(Adjacent(portoUniao, 78))        
    canoinhas.add_adjacent(Adjacent(tresBarras, 12))   
    canoinhas.add_adjacent(Adjacent(mafra, 66))       

    tresBarras.add_adjacent(Adjacent(canoinhas, 12))        
    tresBarras.add_adjacent(Adjacent(saoMateusDoSul, 43))

    saoMateusDoSul.add_adjacent(Adjacent(portoUniao, 87))        
    saoMateusDoSul.add_adjacent(Adjacent(irati, 57)) 
    saoMateusDoSul.add_adjacent(Adjacent(palmeira, 77))   
    saoMateusDoSul.add_adjacent(Adjacent(lapa, 60))   
    saoMateusDoSul.add_adjacent(Adjacent(tresBarras, 43))          

    irati.add_adjacent(Adjacent(pauloFrontin, 75))        
    irati.add_adjacent(Adjacent(saoMateusDoSul, 57))
    irati.add_adjacent(Adjacent(palmeira, 75))
    
    curitiba.add_adjacent(Adjacent(campoLargo, 29))        
    curitiba.add_adjacent(Adjacent(balsaNova, 51))
    curitiba.add_adjacent(Adjacent(araucaria, 37))
    curitiba.add_adjacent(Adjacent(saoJoseDosPinhais, 15))
    
    palmeira.add_adjacent(Adjacent(irati, 75))        
    palmeira.add_adjacent(Adjacent(saoMateusDoSul, 77))       
    palmeira.add_adjacent(Adjacent(campoLargo, 55))    

    mafra.add_adjacent(Adjacent(canoinhas, 66))        
    mafra.add_adjacent(Adjacent(lapa, 57))      
    mafra.add_adjacent(Adjacent(tijucasDoSul, 99))

    campoLargo.add_adjacent(Adjacent(palmeira, 55))
    campoLargo.add_adjacent(Adjacent(balsaNova, 22))
    campoLargo.add_adjacent(Adjacent(curitiba, 29))

    balsaNova.add_adjacent(Adjacent(campoLargo, 22))
    balsaNova.add_adjacent(Adjacent(contenda, 19))
    balsaNova.add_adjacent(Adjacent(curitiba, 51))
  
    lapa.add_adjacent(Adjacent(saoMateusDoSul, 60))
    lapa.add_adjacent(Adjacent(mafra, 57))
    lapa.add_adjacent(Adjacent(tijucasDoSul, 99))

    tijucasDoSul.add_adjacent(Adjacent(mafra, 99))
    tijucasDoSul.add_adjacent(Adjacent(saoJoseDosPinhais, 49))

    araucaria.add_adjacent(Adjacent(curitiba, 37))
    araucaria.add_adjacent(Adjacent(contenda, 18))

    saoJoseDosPinhais.add_adjacent(Adjacent(tijucasDoSul, 49))
    saoJoseDosPinhais.add_adjacent(Adjacent(curitiba, 15))

    contenda.add_adjacent(Adjacent(araucaria, 18))
    contenda.add_adjacent(Adjacent(balsaNova, 19))
    contenda.add_adjacent(Adjacent(lapa, 26))