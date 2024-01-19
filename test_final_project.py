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

if __name__ == '__main__':
    unittest.main()
