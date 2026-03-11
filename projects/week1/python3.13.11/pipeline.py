import sys

import pandas as pd

print('arguments', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame()
print(df.head())

print(f'hello pipeline, month={month}')
