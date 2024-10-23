import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = None

# 3
for field in ['cholesterol','gluc']:
    df.loc[df[field] == 1, field] = 0
    df.loc[df[field] > 1, field] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc','smoke','alco','active','overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable'],as_index=False).value_counts()
    print(df_cat)

    # 7



    # 8
    fig = None


    # 9
    #fig.savefig('catplot.png')
    #return fig
    return None

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
