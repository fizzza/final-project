# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Usage
data_file = 'cpi_food copy.csv'
df = read_data(data_file)
print(df.head())

def plot_line_graph(x_values, y_values, xlabel, ylabel, title):
    plt.plot(x_values, y_values, label='Line Graph')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)  # Show grid
    plt.show()

def plot_bar_graph(x_values, y_values_list, labels, xlabel, ylabel, title, bar_width=0.2):
    for i, y_values in enumerate(y_values_list):
        plt.bar(x_values + i * bar_width, y_values, width=bar_width, label=labels[i])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


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

# Set the bar width 
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

