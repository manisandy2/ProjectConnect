import sqlite3
import json
import pandas as pd

# connect = sqlite3.connect("db.sqlite3")

# cursor = connect.cursor()
# cursor.execute('Create Table if not exists Status (name Text)')

data = pd.read_json("status.json")

print(data.to_string())

# columns = ['name']

# for row in traffic:
#     keys= tuple(row[c] for c in columns)
#     # cursor.executescript('insert into Status values(?,?)',keys)
#     # print(f'{row["id"]} data inserted Succefully')
#     print(keys)

# connect.commit()
# connect.close()