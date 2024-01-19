# final-project
# CPI Data Visualization Project

This project involves data visualization of Consumer Price Index (CPI) data related to different food categories over time.

## Introduction

Consumer Price Index (CPI) is a key economic indicator that measures the average change over time in the prices paid by consumers for a basket of goods and services. This project focuses on visualizing CPI data specifically related to various food categories.

## Motivation

Understanding the trends in CPI for different food items is crucial for consumers, businesses, and policymakers. This project aims to provide insights into how the Consumer Price Index has evolved over the years for specific food-related goods.

## Installation

Make sure you have Python and the required libraries installed. You can install the necessary dependencies using the following command:

```bash
pip install numpy pandas matplotlib

## Code Structure

final_project.py: Python script containing functions for reading data and creating visualisations.

cpi_food.csv: Sample CPI data file.

## Functions

read_data(file_path)
Reads CPI data from a CSV file.

plot_line_graph(x_values, y_values, xlabel, ylabel, title)
Plots a line graph to visualize the trends over time.

plot_bar_graph(x_values, y_values_list, labels, xlabel, ylabel, title, bar_width=0.2)
Plots a bar graph to compare multiple categories over time.

create_dataframe()
Creates a sample DataFrame for visualization.

plot_histograms(df)
Plots histograms for different CPI categories, providing a distribution overview.

plot_box_plots(df)
Plots box plots for different CPI categories, showcasing statistical distributions.

## Data Source

The CPI data used in this project is sourced from The Office of National Statistics, and it represents the CPI values for various food categories over the years 2010 to 2023.


