# AI - Disaster Relief Supply Optimization

## Description  
This project focuses on developing **search algorithms** to optimize the distribution of essential supplies (food, medicine, etc.) in disaster-stricken areas. The system prioritizes critical zones, manages vehicle constraints (capacity, fuel), and adapts to dynamic challenges like weather changes and blocked routes. It aims to maximize coverage, minimize resource waste, and ensure timely deliveries using AI-driven strategies.

### 🎯 Purpose:  
The goal is to apply **AI search algorithms** to solve a real-world logistics problem, emphasizing:  
- Problem formulation as a state-space search  
- Graph-based modeling of zones and routes  
- Comparison of informed (A*, greedy) vs. uninformed (BFS, DFS) search strategies  
- Dynamic simulation (weather, route blockages)  
- Priority-based resource allocation (urgency, population density)  
- Efficient resource management (perishables, fuel)  

### 🚀 Key Features:  
- **Search Problem Formulation**: Define states (vehicle locations, resource levels), actions (move, load/unload), and goal tests (all critical zones served).  
- **Graph Representation**: Model zones as nodes and accessible routes as edges with weights (time, fuel cost).  
- **Algorithm Implementation**:  
  - **Uninformed**: BFS, DFS, Uniform Cost Search (UCS)  
  - **Informed**: A*, greedy best-first  
  - *Improvement*: Genetic Algorithms (example of future work)  
- **Dynamic Simulation**: Adjust route costs/accessibility based on weather (e.g., storms slowing helicopters).  
- **Priority System**: Allocate resources first to high-priority zones (urgency + population).  
- **Resource Constraints**: Track vehicle capacity, fuel limits, and perishable goods decay.  
- **Multi-Vehicle Support**: Drones, trucks, helicopters with unique capabilities/limitations.  

## 📚 Learning Outcomes  
- **Search Algorithms**: Mastered implementation and comparison of AI search techniques.  
- **Graph Modeling**: Built weighted graphs to represent zones, routes, and dynamic obstacles.  
- **Dynamic Adaptation**: Integrated real-time adjustments for weather and route changes.  
- **Team Collaboration**: Used GitHub for version control and Agile workflows.
- **Performance Optimization**: Balanced efficiency (time/fuel) vs. coverage in algorithm design.  

## 🚧 Areas for Improvement  
- **Additional Algorithms**: Implement ant colony optimization or genetic algorithms for swarm intelligence.  
- **Enhanced Variables**: Include vehicle maintenance, driver fatigue, or multi-depot logistics.  

## 👨‍💻 Contributors
- **Alex Araújo Sá** - [Alex Sá](https://github.com/alexaraujosa)
- **Paulo Alexandre Rodrigues Ferreira** - [Paulo Ferreira](https://github.com/pauloarf)
- **Rafael Santos Fernandes** - [DarkenLM](https://github.com/DarkenLM)

## 🛠️ Technologies Used  
- **Language**: Python  
- **Graph Libraries**: NetworkX, OSM
- **Version Control**: GitHub + Git  
- **Documentation**: Markdown, typst (for report)  
