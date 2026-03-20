### `logic.py` – `simulation_medium()`
```mermaid
flowchart TD

    A([Start simulation_medium]) --> B["random.random()"]

    B --> C{Zufallswert < 0.3?}

    C -->|ja| D["simulation_easy()"]
    D --> E[return zufälliger Zug]

    C -->|nein| F["simulation_difficult()"]
    F --> G[return bester Zug]