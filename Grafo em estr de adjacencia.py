class Vertice:
  def __init__(vertice,valor):
    vertice.valor = valor
    vertice.ponteiro = None

class Grafo:
  def __init__(grafo,n_de_vertices):
    grafo.n_de_vertices = n_de_vertices
    grafo.vertices = [None] * n_de_vertices

  def ligaVertices(grafo,valor_vi,valor_vf):
    novo_ver = Vertice(valor_vf)
    novo_ver.ponteiro = grafo.vertices[valor_vi]
    grafo.vertices[valor_vi] = novo_ver

    novo_ver = Vertice(valor_vi)
    novo_ver.ponteiro = grafo.vertices[valor_vf]
    grafo.vertices[valor_vf] = novo_ver
    

  def printGrafo(grafo):
    for i in range(grafo.n_de_vertices):
      print(f"|v{i}|", end="")
      
      vert_atual = grafo.vertices[i]
      while vert_atual:
        print(f" -> v{vert_atual.valor}", end="")
        vert_atual = vert_atual.ponteiro
      print()

grafo = Grafo(5)
grafo.ligaVertices(0, 1)
grafo.ligaVertices(0, 4)
grafo.ligaVertices(1, 2)
grafo.ligaVertices(1, 3)
grafo.ligaVertices(1, 4)
grafo.ligaVertices(2, 3)
grafo.ligaVertices(3, 4)

grafo.printGrafo()
