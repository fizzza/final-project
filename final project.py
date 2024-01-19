import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## Read in the data file.

df = pd.read_csv('cpi_food copy.csv')
df.head()
# Assign x-values and y-values
x_values = df.iloc[:, 0]
y_values = df.iloc[:, 1]

# Plot the line graph
plt.plot(x_values, y_values, label='Line Graph')
plt.xlabel('Year')
plt.ylabel('CPI for Food, Alcoholic Beverages & Tobacco Goods')
plt.title('Time Series Graph: CPI for Food, Alcoholic Beverages & Tobacco Goods Overtime  ')
plt.grid(True)  # Show grid
plt.show()

# Assign x-values and y-values
x_values = df.iloc[:, 0]
y_values = df.iloc[:, 2]

# Plot the line graph
plt.plot(x_values, y_values, label='Line Graph')
plt.xlabel('Year')
plt.ylabel('CPI for Processed Food & Non-Alcoholic Beverages Goods')
plt.title('Time Series Graph: CPI for Processed Food & Non-Alcoholic Beverages Goods Overtime  ')
plt.grid(True)  # Show grid
plt.show()

# Assign x-values and y-values
x_values = df.iloc[:, 0]
y_values = df.iloc[:, 3]

# Plot the line graph
plt.plot(x_values, y_values, label='Line Graph')
plt.xlabel('Year')
plt.ylabel('CPI for Unprocessed Food Goods')
plt.title('Time Series Graph: CPI for Unprocessed Food Goods Overtime  ')
plt.grid(True)  # Show grid
plt.show()

# Assign x-values and y-values
x_values = df.iloc[:, 0]
y1_values = df.iloc[:, 1]
y2_values = df.iloc[:, 2]
y3_values = df.iloc[:, 3]

# Set the bar width (adjust as needed)
bar_width = 0.2

# Plot the bar graph
plt.bar(x_values, y1_values, width=bar_width, label='CPI for Food, Alcoholic Beverages & Tobacco Goods')
plt.bar(x_values + bar_width, y2_values, width=bar_width, label='CPI for Processed Food & Non-Alcoholic Beverages Goods')
plt.bar(x_values + 2 * bar_width, y3_values, width=bar_width, label='CPI for Unprocessed Food Goods')

plt.xlabel('Year')
plt.ylabel('CPI')
plt.title('Bar Graph showing CPIs')
# Show legend
plt.legend()
plt.show()

