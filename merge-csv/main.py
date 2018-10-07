"""Ten skrypt przyjmuje pojedyncze pliki CSV z folderu responses
i łączy je w jeden. 
"""
import os
import tablib

all_data = []
direc = '../responses'
unwanted_columns = [
  'Dodatkowy komentarz dla prowadzącego:',
  'Dodatkowy komentarz dla zespołu PyLight:',
  'Sygnatura czasowa'
]

for fname in sorted(os.listdir(direc)):
    with open(os.path.join(direc, fname)) as f:
        data = f.read()
        all_data.append(tablib.Dataset().load(data))

# make a superset of all headers
headers = set()        
for dataset in all_data:
    headers = headers.union(
      set(
        h for h in dataset.headers
        if h not in unwanted_columns)
    )
    
print(headers)

def make_big_row(row, all_headers):
    return tuple(
        row.get(header) 
        for header in all_headers   
    )


big_table = tablib.Dataset()
big_table.headers = headers
for dataset in all_data:
    for row in dataset.dict:
        big_row = make_big_row(row, headers)
        big_table.append(big_row)
      
with open('../responses_merged.csv', 'w') as f:
    f.write(big_table.export('csv'))
