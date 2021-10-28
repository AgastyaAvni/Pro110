import csv
import statistics
import plotly.express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
fig = ff.crate_distplot([data],['reading_time'],show_hist=False)
fig.show()

popultaion_mean=statistics.mean(data)
print('Mean =',population_mean)
population_standarddeviation=statistics.stdev(data)
print('Standard Daviation = ',population_stand)