
# Formulação do Problema - Distribuição de Alimentos em Zonas Afetadas por Catástrofe Natural

## Tipo:
**Problema de Estado Único Com Necessidade de Planos de Contingência, Determinístico e Dinâmico**.

*Justificação*: Este é um **problema de estado único** porque, inicialmente, o sistema parte de um único estado bem definido: uma configuração inicial das zonas afetadas, veículos disponíveis, distâncias entre as cidades e outros recursos necessários. A cada decisão tomada, como escolher um veículo, traçar uma rota ou fazer uma entrega, o sistema avança para um novo estado, mantendo a total previsibilidade das ações. Ou seja, o problema é **determinístico**, pois as ações que o agente toma não envolvem incertezas, e os efeitos dessas ações são conhecidos.

No entanto, o problema é **dinâmico** porque as condições do ambiente estão sempre a mudar. Por exemplo, as rotas podem ser bloqueadas por tempestades ou quedas de árvores, ou o estado das condições meteorológicas pode alterar-se rapidamente, afetando as viagens dos veículos. Embora o estado atual seja conhecido, a mudança das condições externas, como o clima ou bloqueios imprevistos, exige que o sistema tenha **planos de contingência** para lidar com essas mudanças. O agente (os veículos) precisa de reagir a essas alterações e tomar decisões em tempo real, adaptando-se ao novo estado à medida que ele evolui.

Portanto, o problema é caracterizado por um **estado único inicial**, mas ao longo da execução, as decisões são feitas de forma determinística, levando em conta as mudanças do ambiente, que exigem **ajustes e planos de contingência** para garantir que a distribuição de alimentos seja feita com eficácia.


## Representação:
**Grafo de Municípios e Rotas**.
- **Nós (Vértices)**: Representam os **municípios** ou **zonas afetadas**.
- **Arestas (Ligações entre nós)**: Representam as **rotas** entre os municípios, com **distâncias**, **tempo de viagem**, e **condições** associadas (ex: tempestade, nevoeiro).
- **População e Necessidades**: Cada município tem uma população associada e uma prioridade de necessidade de alimentos.

## Estado Inicial:
- **Posição dos veículos**: Todos os veículos começam no **centro de distribuição** ou num ponto inicial predeterminado (Idealmente Braga).
- **Inventário de alimentos**: Cada veículo tem uma quantidade de alimentos para distribuir.
- **Municípios sem suprimentos**: Nenhuma zona foi atendida.
- **Condições meteorológicas iniciais**: Pode ser definido um cenário inicial com algumas zonas afetadas por tempestades ou nevoeiro (Podemos assumir que inicialmente portugal esta completamente fodido).

## Estado Objetivo:
- **Objetivo Principal**: Distribuir alimentos a todas as zonas afetadas, respeitando as prioridades de cada município (mais crítico, maior população) e considerando as **limitações dos veículos** (capacidade de carga, autonomia, tempo).
- **Objetivo Secundário**: Garantir que as zonas mais críticas recebam assistência **antes de atingirem o limite de tempo crítico**.
- **Meta**: Maximizar o número de zonas atendidas e a quantidade de pessoas assistidas dentro das restrições (tempo e combustível).

## Operadores:
Os operadores correspondem às ações que podem ser tomadas durante a execução do problema. Cada operação altera o estado do sistema de forma previsível.

1. **Escolher um veículo**:
   - **Pré-condição**: O veículo está disponível e no centro de distribuição ou em algum município. O veículo tem combustível suficiente e capacidade para a carga.
   - **Efeito**: O veículo é designado para entregar alimentos numa zona específica.

2. **Escolher uma rota**:
   - **Pré-condição**: O veículo tem combustível suficiente e a rota é viável, levando em consideração as condições meteorológicas e geográficas.
   - **Efeito**: O veículo percorre a rota selecionada, atualizando a posição e o combustível disponível.
   
3. **Realizar uma entrega**:
   - **Pré-condição**: O veículo chegou a um município e tem alimentos para entregar.
   - **Efeito**: A zona recebe alimentos, a população da zona é atendida, e o veículo perde capacidade de carga. A quantidade de alimentos restantes é atualizada.

4. **Ajustar para condições dinâmicas**:
   - **Pré-condição**: Mudanças nas condições, como bloqueios de rotas ou condições meteorológicas adversas, podem afetar a viabilidade de rotas.
   - **Efeito**: O sistema deve recalcular a rota, talvez escolhendo uma nova rota ou reabastecendo o veículo.

5. **Reabastecer veículo**:
   - **Pré-condição**: O veículo está perto de um ponto de reabastecimento e possui combustível suficiente para fazer a entrega.
   - **Efeito**: O combustível do veículo é reabastecido, permitindo que ele continue a sua missão.

## Custo:
O custo associado a cada operação pode ser composto por vários fatores, dependendo da escolha do algoritmo de busca (como A* ou Dijkstra). O **custo total** pode ser uma combinação de:

1. **Distância percorrida**:
   - Custo da distância entre os municípios. Isto pode ser usado para calcular o tempo de viagem ou o custo em termos de combustível.

2. **Combustível utilizado**:
   - Custo do combustível necessário para a viagem. Este pode ser um fator importante, já que veículos como drones ou helicópteros podem ter limitações maiores do que camiões ou comboios.

3. **Condições meteorológicas**:
   - Alteração do custo devido a tempestades, nevoeiro, ou cheias, que podem afetar a velocidade dos veículos ou até mesmo bloquear rotas.

4. **Capacidade do veículo**:
   - Se um veículo transporta mais do que a sua capacidade, há um custo adicional (ou o veículo pode ter de voltar para reabastecer antes de continuar).

5. **Tempo de entrega**:
   - Custo de tempo associado a cada entrega, especialmente se houver uma janela de tempo crítica em que a assistência precisa chegar. O tempo pode ser mais crítico em regiões com maiores necessidades.

## Exemplo de Fórmula para o Custo:
- O **custo de cada ação** pode ser definido como:
  \[
  	ext{Custo da Ação} = 	ext{Distância Percorrida} + 	ext{Combustível Utilizado} + 	ext{Tempo de Viagem} + 	ext{Penalidades por Condições Meteorológicas}
  \]
  
  Onde a **distância percorrida** depende das arestas no grafo, o **combustível utilizado** é proporcional à distância e ao tipo de veículo, e o **tempo de viagem** pode ser ajustado com base na velocidade do veículo e nas condições climáticas.

## Exemplo de Custo de uma Rota:
- Suponha que um camião de entrega tenha que ir de Lisboa a Porto:
  - Distância = 300 km.
  - Combustível utilizado = 0,5 litro/km (camião tem consumo de 0,5 litro por quilómetro).
  - Condições meteorológicas: uma tempestade reduz a velocidade do camião pela metade, aumentando o tempo de viagem.
  - Tempo sem tempestade = 5 horas (300 km / 60 km/h), mas com tempestade = 10 horas (300 km / 30 km/h).
  - O custo de combustível e tempo seria calculado com base nesses valores.

## Resumo da Formulação:

- **Tipo**: Problema de estado único, determinístico.
- **Representação**: Grafo de municípios com distâncias, populações e condições meteorológicas.
- **Estado Inicial**: Veículos no centro de distribuição, municípios sem suprimentos, algumas condições meteorológicas ativas.
- **Estado Objetivo**: Distribuir alimentos para todas as zonas dentro do tempo crítico, priorizando zonas mais afetadas e com maior população.
- **Operadores**: Escolher um veículo, escolher uma rota, realizar uma entrega, ajustar para condições dinâmicas, reabastecer o veículo.
- **Custo**: Distância percorrida, combustível utilizado, tempo de viagem, condições meteorológicas e capacidade dos veículos.

