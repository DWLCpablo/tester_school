from copy import deepcopy


class TabularData: # panie, to Ci nie idzie
    def __init__(self, column_names):
        self.column_names = list(column_names)
        self.columns = {}
        for idx, name in enumerate(column_names):
            self.columns[name] = idx
         # to samo w poprzednich 3 liniach:
        self.columns[name] = {name: idx for idx, name in enumerate(column_names)}
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

my_tab = TabularData(['Name', 'Age', 'Shoe size'])
my_tab.append(['pablo', 33, 45])
print(my_tab.column_names)
my_tab.append(['a', 2, 3])
my_tab.append(['Gosia', 29, 38])
my_tab.append(['Ciszewski', 30, 42])
print(my_tab._rows)
print(my_tab.get_row(2))
print(my_tab.rows_count())
print(my_tab.get_column('Age'))


