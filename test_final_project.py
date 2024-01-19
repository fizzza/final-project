# test_final_project.py

import unittest
from final_project import process_data, plot_line_graph, plot_bar_graph

class TestFinalProject(unittest.TestCase):

    def test_process_data(self):
        data_file = 'cpi_food copy.csv'  # adjust the path if needed
        df = process_data(data_file)
        self.assertIsNotNone(df)
        # Add more assertions based on your expectations for the processed data

    def test_plot_line_graph(self):
        # Add test for plot_line_graph function
        pass

    def test_plot_bar_graph(self):
        # Add test for plot_bar_graph function
        pass

    def test_process_data(self):
        data_file = 'cpi_food copy.csv'  # adjust the path if needed
        df = process_data(data_file)
        self.assertIsNotNone(df)
        # Add more assertions based on your expectations for the processed data

    def test_plot_line_graph(self):
        # Example test for plot_line_graph function
        x_values = [1, 2, 3, 4]
        y_values = [5, 6, 7, 8]
        xlabel = 'X-axis'
        ylabel = 'Y-axis'
        title = 'Test Line Graph'
        result = plot_line_graph(x_values, y_values, xlabel, ylabel, title)
        self.assertIsNone(result)  # Modify based on the expected behavior

    def test_plot_bar_graph(self):
        # Example test for plot_bar_graph function
        x_values = [1, 2, 3, 4]
        y_values_list = [[5, 6, 7, 8], [9, 10, 11, 12]]
        labels = ['Bar1', 'Bar2']
        xlabel = 'X-axis'
        ylabel = 'Y-axis'
        title = 'Test Bar Graph'
        result = plot_bar_graph(x_values, y_values_list, labels, xlabel, ylabel, title)
        self.assertIsNone(result)  # Modify based on the expected behavior


if __name__ == '__main__':
    unittest.main()

