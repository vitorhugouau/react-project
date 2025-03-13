# Exercício 3 - Mapa Mundi


class State:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area  # Em km²

    def density(self):
        """Retorna a densidade populacional do estado."""
        return self.population / self.area if self.area > 0 else 0

    def __str__(self):
        return f"Estado: {self.name}, População: {self.population}, Área: {self.area} km², Densidade: {self.density():.2f} hab/km²"


class Country:
    def __init__(self, name, capital, states=None):
        self.name = name
        self.capital = capital
        self.states = states if states else []

    def add_state(self, state):
        """Adiciona um estado ao país."""
        self.states.append(state)

    def total_population(self):
        """Retorna a população total do país."""
        return sum(state.population for state in self.states)

    def __str__(self):
        return f"País: {self.name}, Capital: {self.capital}, População Total: {self.total_population()}"


class WorldMap:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        """Adiciona um país ao mapa mundi."""
        self.countries.append(country)

    def total_population(self):
        """Retorna a população total do mundo considerando os países no mapa."""
        return sum(country.total_population() for country in self.countries)

    def __str__(self):
        return f"Mapa Mundi - Total de Países: {len(self.countries)}, População Global: {self.total_population()}"


# Exemplo de uso
if __name__ == "__main__":
    # Criando estados
    sp = State("São Paulo", 45000000, 248222)
    rj = State("Rio de Janeiro", 17366189, 43780)

    # Criando um país e adicionando estados
    brasil = Country("Brasil", "Brasília")
    brasil.add_state(sp)
    brasil.add_state(rj)

    # Criando o mapa mundi e adicionando o país
    world = WorldMap()
    world.add_country(brasil)

    # Exibindo informações
    print(sp)
    print(rj)
    print(brasil)
    print(world)
