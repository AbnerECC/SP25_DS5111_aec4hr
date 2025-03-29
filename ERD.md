



erDiagram
    STOCK }|--|{ STOCK-VALUE : has
    STOCK-VALUE ||--|| VALUE-HIGH : Peaks
    STOCK-VALUE ||--|| VALUE-LOW : Valleys
    STOCK {
        string symbol PK     
    }
    VALUE-HIGH{
        string symbol PK, FK
        float High
        datetime datetime
    }
    VALUE-LOW{
        string symbol PK, FK
        float Low
        datetime datetime
    }
    STOCK-VALUE {
        string symbol PK, FK
        datetime datetime PK
        float price
        float volume
    }

