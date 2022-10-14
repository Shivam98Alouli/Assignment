#Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

import pandas as pd
x=pd.date_range('1st Jan, 2023','10th Feb, 2023')
print("series of dates\n",x)
