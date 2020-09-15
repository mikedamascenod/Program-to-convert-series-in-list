# A Pandas program to convert series in lists to one series.

import pandas as pd

s = pd.Series([
    ['Blue', 'Red', 'white'],
    ['Red', 'Black'],
    ['Green']])
print("Original series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)
