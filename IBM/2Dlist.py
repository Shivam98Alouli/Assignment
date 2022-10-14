#Create 2D list to DataFrame

import pandas as pd
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df = pd.DataFrame(lists, columns=['A', 'B','C'])
print(df)
