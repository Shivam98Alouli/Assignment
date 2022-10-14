#Create a data frame with 3 rows and 2 columns

import pandas as pd
data = [['tom', 10], ['nancy', 15],['john',18]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
