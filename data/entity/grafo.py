class Grafo:
    def __init__(self, name):
        self.name = name
        self.vertices = {}
        self.ProductosRecomendados = []

        self.mayor = 0
        self.i_mayor = 0

    def Agregar_Vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen][destino] = peso

    def MostrarBiblioteca(self):
        print("----------------------")
        print(self.vertices)

    def mostrar_vertices(self):
        for nodo in self.vertices:
            print(nodo, "-->", [i for i in self.vertices[nodo]], )

    def PesoMaximo(self):
        print("Peso maximo: {} Indice: {}".format(self.mayor, self.i_mayor))


