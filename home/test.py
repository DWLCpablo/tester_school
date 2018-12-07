import copy
import json


class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {name: idx for idx, name in enumerate(column_names)}
        if len(column_names) > len(self._columns):
            raise ValueError('Column names have to be unique!')
        self.rows = []

    def get_row(self, row_no):
        if row_no - 1 > len(self.rows) or row_no <= 0:
            raise IndentationError('Row_no is higher than available rows')
        return self.rows[row_no - 1]

    def get_column(self, column_name):
        columns = []
        column_no = self._columns[column_name]
        if column_name not in self.column_names:
            raise KeyError('Column_no is higher than available columns')
        [columns.append(record[column_no]) for record in self.rows]
        return columns

    def append(self, new_row):
        if len(new_row) == len(self.column_names):
            self.rows.append(new_row)
        else:
            raise ValueError('New_row has different size than columns')

    def get_rows_count(self):
        return len(self.rows)

    def get_list(self):
        return copy.deepcopy(self.rows)

    def __len__(self):
        return len(self.rows)

    def __str__(self):
        return str(self.rows)

    # to json
    # from json
    # to json file
    # from json file

    def to_dict(self):
        return {'columns': self.column_names, 'rows': self.rows}

    @staticmethod
    def from_dict(loaded_json):
        new_table = TabularData(loaded_json['columns'])
        for row in loaded_json['rows']:
            new_table.append(row)
        return new_table

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_data):
        return TabularData.from_dict(json.loads(json_data))

    def to_json_file(self, output_file):
        return json.dump(self.to_dict(), output_file)

    @staticmethod
    def from_json_file(json_data):
        new_table = TabularData.from_dict(json.load(json_data))
        return new_table


if __name__ == '__main__':
    column_names = ['first_name', 'second_name', 'age']
    data = TabularData(column_names)
    print(column_names)
    data.append(['Lukasz', 'Tkaczyk', 20])
    data.append(['Bartek', 'Jakis', 50])
    print(data.get_list())

    print(data.get_row(2))
    print()
    print(data.get_column('first_name'))
    print(data.get_column('age'))
    print()

    print(data.get_rows_count())


    print()
    print(data.to_json())
    print()
    print(data.from_json(data.to_json()))
    print()
