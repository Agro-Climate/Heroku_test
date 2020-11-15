import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

print(dash.__version__)
df = pd.read_csv('iris2.csv')
print (df.iloc[0])
