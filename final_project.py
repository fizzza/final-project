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

def create_dataframe():
    data = {
        'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'CPI for Food, Alcoholic Beverages & Tobacco Goods': [148, 160, 154, 150, 157, 153, 145, 146, 143, 140, 139, 159, 166, 161],
        'CPI for Processed Food & Non-Alcoholic Beverages Goods': [58, 64, 62, 58, 61, 60, 56, 57, 55, 54, 54, 62, 64, 69],
        'CPI for Unprocessed Food Goods': [50, 54, 50, 48, 51, 50, 47, 46, 46, 46, 45, 52, 52, 50]
    }
    df = pd.DataFrame(data)
    return df

def plot_histograms(df):
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))

    df['CPI for Processed Food & Non-Alcoholic Beverages Goods'].plot(kind='hist', bins=10, edgecolor='black', ax=axes[0], title='CPI for Processed Food & Non-Alcoholic Beverages Goods')
    df['CPI for Unprocessed Food Goods'].plot(kind='hist', bins=10, edgecolor='black', ax=axes[1], title='CPI for Unprocessed Food Goods')
    df['CPI for Food, Alcoholic Beverages & Tobacco Goods'].plot(kind='hist', bins=10, edgecolor='black', ax=axes[2], title='CPI for Food, Alcoholic Beverages & Tobacco Goods')

    plt.tight_layout()
    plt.show()


# Create a DataFrame
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'CPI for Food, Alcoholic Beverages & Tobacco Goods': [148, 160, 154, 150, 157, 153, 145, 146, 143, 140, 139, 159, 166, 161],
    'CPI for Processed Food & Non-Alcoholic Beverages Goods': [58, 64, 62, 58, 61, 60, 56, 57, 55, 54, 54, 62, 64, 69],
    'CPI for Unprocessed Food Goods': [50, 54, 50, 48, 51, 50, 47, 46, 46, 46, 45, 52, 52, 50]
}

df = pd.DataFrame(data)

# Create histograms for the second, third, and fourth columns
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))

df['CPI for Processed Food & Non-Alcoholic Beverages Goods'].plot(kind='hist', bins=10, edgecolor='black', ax=axes[0], title='CPI for Processed Food & Non-Alcoholic Beverages Goods')
df['CPI for Unprocessed Food Goods'].plot(kind='hist', bins=10, edgecolor='black', ax=axes[1], title='CPI for Unprocessed Food Goods')
df['CPI for Food, Alcoholic Beverages & Tobacco Goods'].plot(kind='hist', bins=10, edgecolor='black', ax=axes[2], title='CPI for Food, Alcoholic Beverages & Tobacco Goods')

plt.tight_layout()
plt.show()

def create_dataframe():
    data = {
        'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'CPI for Food, Alcoholic Beverages & Tobacco Goods': [148, 160, 154, 150, 157, 153, 145, 146, 143, 140, 139, 159, 166, 161],
        'CPI for Processed Food & Non-Alcoholic Beverages Goods': [58, 64, 62, 58, 61, 60, 56, 57, 55, 54, 54, 62, 64, 69],
        'CPI for Unprocessed Food Goods': [50, 54, 50, 48, 51, 50, 47, 46, 46, 46, 45, 52, 52, 50]
    }
    df = pd.DataFrame(data)
    return df

def plot_box_plots(df):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    df.boxplot(column='CPI for Processed Food & Non-Alcoholic Beverages Goods', ax=axes[0])
    axes[0].set_title('CPI for Processed Food & Non-Alcoholic Beverages Goods Box Plot')

    df.boxplot(column='CPI for Unprocessed Food Goods', ax=axes[1])
    axes[1].set_title('CPI for Unprocessed Food Goods Box Plot')

    df.boxplot(column='CPI for Food, Alcoholic Beverages & Tobacco Goods', ax=axes[2])
    axes[2].set_title('CPI for Food, Alcoholic Beverages & Tobacco Goods Box Plot')

    plt.tight_layout()
    plt.show()

# Create a DataFrame
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'CPI for Food, Alcoholic Beverages & Tobacco Goods': [148, 160, 154, 150, 157, 153, 145, 146, 143, 140, 139, 159, 166, 161],
    'CPI for Processed Food & Non-Alcoholic Beverages Goods': [58, 64, 62, 58, 61, 60, 56, 57, 55, 54, 54, 62, 64, 69],
    'CPI for Unprocessed Food Goods': [50, 54, 50, 48, 51, 50, 47, 46, 46, 46, 45, 52, 52, 50]
}

df = pd.DataFrame(data)

# Create box plots for the second, third, and fourth columns
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

df.boxplot(column='CPI for Processed Food & Non-Alcoholic Beverages Goods', ax=axes[0])
axes[0].set_title('CPI for Processed Food & Non-Alcoholic Beverages Goods Box Plot')

df.boxplot(column='CPI for Unprocessed Food Goods', ax=axes[1])
axes[1].set_title('CPI for Unprocessed Food Goods Box Plot')

df.boxplot(column='CPI for Food, Alcoholic Beverages & Tobacco Goods', ax=axes[2])
axes[2].set_title('CPI for Food, Alcoholic Beverages & Tobacco Goods Box Plot')

plt.tight_layout()
plt.show()

