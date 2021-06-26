import math as mt

class R_euler:
    def __init__(self, vertices=0, faces=0, arestas=0):
        self.vertices = vertices
        self.faces = faces
        self.arestas = arestas

    def validar(self):
        if self.vertices + self.faces == self.arestas + 2:
            return True
        else:
            return False

    def know_arestas(self):
        self.arestas = (self.faces + self.vertices) - 2
        return self.arestas

    def know_faces(self):
        self.faces = (self.arestas + 2) - self.vertices
        return self.faces

    def know_vertices(self):
        self.vertices = (self.arestas + 2) - self.faces
        return self.vertices

class Platão:
    def __init__(self, vertices=0, faces=0, arestas=0):
        self.vertices = vertices
        self.faces = faces
        self.arestas = arestas

    def validar(self):
        valido = R_euler(self.vertices, self.faces, self.arestas)

        if (self.arestas - self.faces == self.faces
                and self.arestas / self.vertices == self.vertices
                and valido.validar()):
            return True
