import copy
import json

class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {name: idx for idx, name in enumerate(column_names)}
        if len(column_names) > len(self._columns):
            raise ValueError('Column names have to be unique!')
        self.rows = []

    def append_row(self, data):
        if len(data) != len(self._columns):
            raise ValueError('To insert into table, you must specify ' + str(len(self._columns)) + ' parameters.')
        self.rows.append(data)


    def get_row(self, number):
        if number <= 0 or number > len(self.rows):
            raise ValueError('Invalid row number: ', number)
        return self.rows[number]

    def get_column1(self, col_name):
        idx = self._columns[col_name]
        values = []
        for row in self.rows:
            values.append(row[idx])
        return values


    def get_column(self, col_name): # to kurła nie działa ???!?!?!?!
        if col_name not in self._columns:
            raise KeyError('Unknown key name: ', col_name)
        idx = self._columns[col_name]
        values = []
        for row in self.rows:
            values.append(row[idx])
        return values

    def rows_count(self):
        return len(self.rows)

    def to_json(self):
        target = {}
        target['columns'] = self._columns
        target['rows'] = self.rows
        return json.dumps(target)

    def to_dict(self):
        return {'columns': self.column_names, 'rows': self.rows}

    @staticmethod
    def from_dict(data):
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    @staticmethod
    def from_json(data):  # moje
        result = TabularData(data['columns'])
        for row in data['rows']:
            result.append(row)
        return result

    @staticmethod
    def from_json1(json_data):
        return TabularData.from_dict(json.loads(json_data))


if __name__ == '__main__':
    table = TabularData(['Name', 'Age', 'Shoe size'])
    #print(table.column_names)
    #print(table.columns)
    #print(table.rows)
    table.append_row(['Pablo', 33, 45])
    table.append_row(['Karina', 32, 39])
    table.append_row(['Jacek', 5, 28])
    table.append_row(['Agatejszyn', 1, 20])
    #print(table)
    #print(table.rows)
    #print(table.column_names)
    #print(table.get_row(1))
    #print(table.get_column('Name'))
    #print(table.rows_count())
    print(table.to_json())
    json_data = table.to_json()
    #print(table.from_json(json_data))
    #json_data = table.to_dict()
    #print(table.to_dict())
    #print(table.from_dict(json_data))
    print(table.from_json1(json_data))
