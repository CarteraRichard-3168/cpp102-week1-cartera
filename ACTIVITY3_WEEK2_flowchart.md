```mermaid
flowchart TD
    A([Start]) --> B[/Input number/]
    B --> C{number MOD 2 = 0?}
    C -- Yes --> D[/Display "Even"/]
    C -- No --> E[/Display "Odd"/]
    D --> F([End])
    E --> F
```
