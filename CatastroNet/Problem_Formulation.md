# Formulação do Problema

- *Tipo:* Problema de estado único, não determinístico.
  (Estado único pois sabemos o grafo de ante mão e saimos do mesmo sitio.)
  (Não deterministico pq o ambiente é dinámico, o que leva a que uma solução ideal neste momento não o seja no proximo)
  (Definr uma análise Episódica).
- *Representação:*
  - Grafo.
  - Cidades necessitadas.
  - Arestas são distancias.
  - Duplas arestas para cidades devido a transportes aéros. Distancia Euclidiana?
  - Zona costeira? Arestas de transporte aquatico?
  - Pontos de reabastecimento.
- *Estado inicial:* A frota e os recursos estão localizados num armazém central.
- *Estado Objetivo:* Maximizar o número de pessoas assistidas dentro de um tempo limitado.
- *Operadores:*
  - _Operação1_:
  - (pré-condição) .
  - (pré-condição) .
  - *(efeito)* .
- *Custo:* Depende do Tempo, do combustivel, valor monetário?.


Coisas a pesquisar
(Open street map) - Para criação do grafo
(Hamiltonian Circuits and the Traveling Salesman Problem) - Para algoritmo

- Vamos proceder com ACO (Ant colony optimization)
- More information [here](https://www.sciencedirect.com/science/article/pii/S136655450700021X?casa_token=VEFaMiTImLkAAAAA:we1JoK1RsG7ATLda0LUacIV1TIRIAwVfaZjoHsy03o07Vo6KOaPb7Ktag8JOJvn5_rrWb4EPFdY)

- Reinforcement learning (Possibilidade, mas é deep learning)