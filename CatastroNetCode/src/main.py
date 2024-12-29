import osm.PortugalCompleto
from src.Graph import Graph


def main():
    #Comentar no caso de não se querer gerar nova informação. (Em principio não será mais necessário)
    #osm.PortugalCompleto.run()

    #Aparentemente a função load corre logo que o objeto é criado
    grafo = Graph()

    print("LETS GO")

if __name__ == "__main__":
    main()