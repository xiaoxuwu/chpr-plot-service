import pandas as pd
import pdb
from internal.models import *

def process_raw_data(plt_md):
    #pdb.set_trace()
    if plt_md.data_type == PlotMetadata.TYPES[0][0] or plt_md.data_type == PlotMetadata.TYPES[1][0]:
        raw_data = pd.read_csv(plt_md.raw_data.path)
        processed_df = pd.DataFrame(raw_data.groupby('race').race.count())
        processed_df.columns = ['count']
        return processed_df
    
    if plt_md.data_type == PlotMetadata.TYPES[2][0]:
        raw_data = pd.read_csv(plt_md.raw_data.path)
        processed_df = pd.DataFrame(raw_data.groupby(['race','year']).year.count())
        processed_df.columns = ['count']
        return processed_df

def processed_data_to_chart(plt_md):
    if plt_md.data_type == PlotMetadata.TYPES[0][0] or plt_md.data_type == PlotMetadata.TYPES[1][0]:
        chart_data = dict()
        data_df = pd.read_csv(plt_md.processed_data.path)
        for index, row in data_df.iterrows():
            chart_data[row.race] = row['count']
        return chart_data
    if plt_md.data_type == PlotMetadata.TYPES[2][0]:
        #DS process to chart additions below
        chart_data = dict()
        data_df = pd.read_csv(plt_md.processed_data.path)
        for index, row in data_df.iterrows():
            if row.year == 2001:
                chart_data[row.race] = [row['count']]
            else:
                chart_data[row.race].append(row['count'])
        return chart_data
