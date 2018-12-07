import json
import copy

class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {}
        for idx, name in enumerate(column_names):
            self._columns[name] = idx
        # self._columns = {name: idx for idx, name in enumerate(column_names)} <-- to samo co powyższe 3 linijki
        if len(column_names) > len(self._columns):
            raise ValueError("Column names have to be unique.")
        self._rows = []

    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError("Invalid row number:", row_no)
        return self._rows[row_no]

    def get_column(self, col_name):
        if col_name not in self._columns:
            raise KeyError("Unknown column: ", col_name)
        idx = self._columns[col_name]

        values = []
        for row in self._rows:
            values.append(row[idx])
        return values

        # return [row[idx] for row in self._rows] <--- to samo co powyższe 4 linijki (nie trzeba values = [])

    def append(self, new_row):
        if len(new_row) != len(self._columns):
            raise ValueError("Row should have size ", len(self._columns))
        self._rows.append(list(new_row))

    def rows_count(self):
        return len(self._rows)
        pass

    def to_list(self):
        return copy.deepcopy(self._rows)

    def __len__(self):  #definiuje, żeby bezpośrednie wywołanie len zwracało długość
        return len(self._rows)

    def __str__(self):  #definiuje, żeby zamieniać cały obiekt na string
        return str(self._rows)

    def to_dict(self):
        return {'columns':self.column_names, 'rows':self._rows}

    def to_json(self):
        return json.dumps(self.to_dict())

    def from_dict(self, data):
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    def from_json(self, json_data):
        return TabularData.from_dict(json.loads(json_data))

if __name__ == '__main__':
    table = TabularData(['Name', 'Age', 'Shoe size'])
    #print(table.column_names)
    #print(table.columns)
    #print(table.rows)
    table.append(['Pablo', 33, 45])
    table.append(['Karina', 32, 39])
    table.append(['Jacek', 5, 28])
    table.append(['Agatejszyn', 1, 20])
    #print(table._rows)
    #print(table)
    #print(table.column_names)
    #print(table.get_row(1))
    #print(table.get_column('Shoe size'))
    #print(table.rows_count())
    #print(table.to_dict())
    #print(table.to_json())
    #print(table.from_dict(table.to_dict()))
    serialized = table.to_json()
    print(table.from_json(seialized(table.to_dict)))

    """def to_dict(self):
    return {'columns': self.column_names, 'rows': self._rows}

@staticmethod
def from_dict(data):
    table = TabularData(data['columns'])
    for row in data['rows']:
        table.append(row)
    return table

def to_json(self):
    return json.dumps(self.to_dict())

@staticmethod
def from_json(json_data):
    return TabularData.from_dict(json.loads(json_data))

def to_json_file(self, output_file):
    return json.dump(self.to_dict(), output_file)

@staticmethod
def from_json_file(json_file):
    return TabularData.from_dict(json.load(json_file))"""