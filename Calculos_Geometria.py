
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

class P_regular:
    def __init__(self, vertices=0, faces=0, arestas=0):
        self.vertices = vertices
        self.faces = faces
        self.arestas = arestas

    def validar(self):
        if (self.vertices - self.arestas + self.faces) == 2:
            return True
        else:
            return False

    def tipo(self):
        if self.faces < 6:
            return 'Tetraedro'
        elif self.faces < 8:
            return 'Hexaedro'
        elif self.faces < 12:
            return 'Octaedro'
        elif self.faces < 20:
            return 'Dodecaedro'
        elif self.faces == 20:
            return 'Icosaedro'
        else:
            return '< Desconhecido >'