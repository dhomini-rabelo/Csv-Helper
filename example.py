from main import CsvHelper


csv = CsvHelper('school')

csv.create(['student', 'room'])

csv.fill_one(['John', 'ROOM A'])

csv.fill_many([
    ['David', 'ROOM B'],
    ['Peter', 'ROOM A'],
])

names = ['Mary', 'Jamie']
rooms = ['ROOM B', 'ROOM A']

csv.fill_by_columns(names, rooms)

csv.del_line(2)

csv.insert_data(2, ['Robert', 'ROOM C'])

csv.view()