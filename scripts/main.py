import os
import pandas as pd
from matplotlib import pyplot
import random

def plot(series_df, term='base_station', feeling_lucky=False):
    term = series_df.columns[random.randint(0, series_df.shape[0])] if feeling_lucky else term
    series = series_df[term] if not feeling_lucky else series_df[term]
    series.plot()
    pyplot.title(term)
    pyplot.show()

series_df = pd.read_csv(os.path.join('data', 'timeseries_10k.csv')).transpose().reset_index()
series_df.columns = series_df.iloc[0]
series_df = series_df.drop(series_df.index[0])
plot(series_df, feeling_lucky=True)
print()
