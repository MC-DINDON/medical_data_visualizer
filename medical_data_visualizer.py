import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height']/100)**2)).apply(lambda x: 1 if x > 25 else 0)

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
    df_cat.rename(columns={'count':'total'},inplace=True)
    print(df_cat)

    # 7


    # 8
    fig = sns.catplot(x="variable", y='total',
                hue="value", col="cardio",
                data=df_cat, kind='bar').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    q1 = (df['ap_lo'] <= df['ap_hi'])
    q2 = (df['height'] >= df['height'].quantile(0.025))
    q3 = (df['height'] <= df['height'].quantile(0.975))
    q4 = (df['weight'] >= df['weight'].quantile(0.025))
    q5 = (df['weight'] <= df['weight'].quantile(0.975))

    df_heat = df[q1 & q2 & q3 & q4 & q5]

    # 12
    corr = df_heat.corr(method="pearson")

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(corr, mask=mask, linewidths=1, annot=True, square=True,fmt=".1f",center=0.08,cbar_kws={"shrink":0.5})

    # 16
    fig.savefig('heatmap.png')
    return fig
