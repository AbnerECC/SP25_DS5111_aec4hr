import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Connect to the Databse

conn = snowflake.connector.connect(
  user ='aec4hr@virginia.edu',
  password = 'DS5111aec4hr',
  account = 'rja95216',
  warehouse = 'COMPUTE_WH',
  database = 'DATA_SCIENCE',
  schema = 'AEC4HR',
  role = 'DS5111_DBT')
  
query = "SELECT * FROM NUMBERS"

# Load data into a dataframe

df = pd.read_sql(query, conn)

conn.close()

# Chart Analysis of Values

sns.set_theme(style="darkgrid", palette="muted")
ax = sns.stripplot(data=df, x='PRICE', y='SOURCE', legend = False)
ax.set(ylabel='')


# Group the top 8 recprds tp show changing prices
grouped = df.groupby('SYMBOL', as_index=False)['PRICE_PERCENT_CHANGE'].max()
top_n_symbols = grouped.nlargest(15, 'PRICE_PERCENT_CHANGE')
filtered_records = df[df['SYMBOL'].isin(top_n_symbols['SYMBOL'])]
sns.set_theme(style="darkgrid")

sns.lineplot(data=filtered_records, x='TIMESTAMP', y='PRICE', hue='SYMBOL', style='SOURCE')

# Remove x-axis markers
plt.xticks([])
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.title('Price Change by Symbol Over Time')

# Move the legend outside of the chart
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()


# Create the price plot
sns.lineplot(data=df, x='TIMESTAMP', y='PRICE_PERCENT_CHANGE', hue='SOURCE', errorbar=None)

# Set plot labels and title
plt.xlabel('Timestamp')
plt.ylabel('Price Percent Change')
plt.title('Price Percent Change by Source Over Time')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.show()