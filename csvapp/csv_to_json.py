import json
import pandas as pd


class CsvToJson:
    """
    This class is used for convert csv data into nested json tree.
    """

    def __init__(self, csv_data):
        """
        Initializing class and assign variables default values
        """
        self.max_column = 0
        self.csv_data = csv_data
        self.total_column = 0

    def tree_create(self):
        """
        - Find max_column depth in csv
        - Find total_column length from csv data
        - This function is used to create main node and push all child into it.
        """
        self.max_column = int(len(self.csv_data.columns) / 3)
        self.total_column = int(len(self.csv_data.columns))
        return json.dumps(self.create_parent_nodes(1, self.csv_data), indent=4)

    def create_parent_nodes(self, start, csv_data):
        """
        - This function is used to create all parents nodes from csv
        - Calls create_child_nodes function inside parent loop to create n level children data
        :parameters:
            start - this is refer to start index.
            csv_data - get the values from csv_data.
        """
        list_to_check_id = []
        parent_lists = []
        if start < self.total_column:
            for row in csv_data.values:
                if str(row[start]) != 'nan':
                    if row[start + 1] not in list_to_check_id and row[start + 1] is not None:
                        list_to_check_id.append(row[start + 1])
                        parent_lists.append({
                            'label': row[start].strip(),
                            'id': str(int(row[start + 1])).strip(),
                            'link': row[start + 2].strip(),
                            'children': self.create_child_nodes(1, row, csv_data, start + 3)
                        })
        return parent_lists

    def create_child_nodes(self, index, current_data, csv_data, start):
        """
        This function is used to create child nodes add data into n level children tree.
        :parameters:
            index - this is refer to the loop index
            current_data - this is refer to current parent and child data to compare with row data.
            csv_data - get the values from csv_data
            start - data will be added as per level
        """
        child = []
        list_to_check_id = []
        if start < self.total_column:
            for row in csv_data.values:
                if current_data[index + 1] == row[index + 1]:
                    if str(row[start]) != 'nan':
                        if row[start + 1] not in list_to_check_id and row[start] is not None:
                            list_to_check_id.append(row[start + 1])
                            child.append({
                                'label': row[start].strip(),
                                'id': str(int(row[start + 1])).strip(),
                                'link': row[start + 2].strip(),
                                'children': self.create_child_nodes(index + 2, row, csv_data, start + 3)
                            })

        return child
