import json
import copy

class TabularData: # panie, to Ci nie idzie
    def __init__(self, column_names):
        self.column_names = list(column_names)
        self.columns = {}
        for idx, name in enumerate(column_names):
            self.columns[name] = idx
         # to samo w poprzednich 3 liniach:
        #self.columns[name] = {name: idx for idx, name in enumerate(column_names)}
        if len(column_names) > len(self.columns):
            raise ValueError('Column names have to be unique.')
        self._rows = []  # _rows()  znaczy, że pole _ jest 'prywatne', by nie eksponować atrybutu dla użytkownika, nie może ich ruszać, modyfikować etc

    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError('Invalid row number: ', row_no)
        return self._rows[row_no]

    def get_column(self, col_name): # tego nie zrobiłeś
        if col_name not in self.columns:
            raise KeyError('Unknown key name: ', col_name)
        idx = self.columns[col_name]
        values = []
        for row in self._rows:
            values.append(row[idx])
        return values


    def get_column_list_expressions(self, col_name):
        if col_name not in self.columns:
            raise KeyError('Unknown key name: ', col_name)
        idx = self.columns[col_name]
        return [row[idx] for row in self._rows]

    def append(self, new_row):
        if len(new_row) != len(self.columns):
            raise ValueError('Row should have size ', len(self.columns))
        self._rows.append(new_row)

    def rows_count(self):
        return len(self._rows)

    def to_list(self):
        return deepcopy(self._rows)

    def __len__(self):      # nadpisujesz len() dla klasy
        return len(self._rows)

    def __str__(self):  # nadpisujesz str() dla klasy
        return str(self._rows)

    def to_dict(self):
        target = {}
        target['columns'] = self.column_names
        target['rows'] = self._rows
        return json.dumps(target)

    def to_json(self):
        target = {}
        target['columns'] = self.column_names
        target['rows'] = self._rows
        return json.dumps(target)

    def to_json1(self):
        return json.dumps(self.to_dict)

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    @staticmethod
    def from_json1(self):
        return TabularData.from_dict(json.loads(json_file))

    @staticmethod
    def from_dict():
        data = json.loads(json_data)
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table


    def to_json_file(self, output_file):
        target = {}
        target['columns'] = self.column_names
        target['rows'] = self._rows
        return json.dump(target, output_file) #dump!! a nie dumps!!!

    def to_json_file1(self, output_file):
        return json.dump(self.to_dict(), output_file)

    @staticmethod
    def from_json_file(json_data):
        data = json.load(json_data)
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    @staticmethod
    def from_json_file1(json_file):
        return TabularData.from_dict(json.loads(json_file))


my_tab = TabularData(['Name', 'Age', 'Shoe size'])
my_tab.append(['pablo', 33, 45])
print(my_tab.column_names)
my_tab.append(['a', 2, 3])
my_tab.append(['Gosia', 29, 38])
my_tab.append(['Ciszewski', 30, 42])
print(my_tab._rows)
print(my_tab.get_row(2))
print(my_tab.rows_count())
#print(my_tab.get_column('Age'))
json_data = my_tab.to_json()
#print(my_tab.to_json())
#print(my_tab.from_json(json_data))
#table2 = TabularData.from_json(json_data)


with open('tabular_data.json', 'wt') as json_file:
    my_tab.to_json_file(json_file)

with open('tabular_data.json', 'rt') as json_file:
    my_tab.from_json_file(json_file)