# Report on the Entity Relationship Diagram for the Snowflake DB

- The entity relationship diagram serves as a blueprint for the SQL database that is used for this gainers repository and databse. It should provide context on the tables and columns included as well as framing for ways to restructure the data if desired.

## Use Cases:

- First a simple drop down of the stocks that this datset contains for users to know where to query for a potential stock. Then two different branching tables the first is Stock-Volume, which includes the trading volume for all the stocks by date time. The next is a Stock-Value that includes the value of the stock at a point in time. Two more child tables are included that have the highest and lowest values of stocks present as well as when they occured.

## Methods:
  
- This data was first sourced from various sites including yahoo and wall street journal. Next it had a module created to automate processing of these respective data sources along with a factory to create additional sourcing if desired. From there processing steps included normalizing both data sets to convert them to the appropriate data types and normalize column values.

## Summary:

- This dataset provides helpful summary statistics on various stock values. It includes the below ERD which can be used in Mermaid Live to visualize the dataset. For future research potentially expanding on trading volume independent of stocks may give insight on if some days have more expected activitiy than others. Additional research may be useful in visualizing if a certain price change threshold predicts a stock being removed from active trading.


![Editor _ Mermaid Chart-2025-03-29-020320](https://github.com/user-attachments/assets/28d5f14b-97b1-4183-a1b2-cc0c55b41289)


erDiagram
    STOCK }|--|{ STOCK-VALUE : has
    STOCK }|--|{ STOCK-VOLUME : traded
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
    }
    STOCK-VOLUME {
        string symbol PK, FK
        datetime datetime PK
        float volume 
    }



