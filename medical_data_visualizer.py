#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df.weight/((df.height/100)**2) > 25).astype(int)

# 3
df["cholesterol"] = (df.cholesterol>1).astype(int)
df["gluc"] = (df.gluc>1).astype(int)

# %%
# 4
def draw_cat_plot():
    # MARK: Important!!! 
    # I didn't use the matplotlib to configure the plot. I configured the plot directly using seaborn. This results in a failed unit test although the task is completed.
    
    # 5
    #%%
    df_cat = pd.melt(df,id_vars="cardio",value_vars=("cholesterol","gluc","smoke","alco","active","overweight"))


    # 6
    df_cat = df_cat.groupby("cardio").value_counts().reset_index(name=("total"))

    # 7
    x_order = sorted(df_cat.variable.unique().tolist())
    sns.catplot(data=df_cat,x="variable",y="total",col="cardio",hue="value",order=x_order,kind="bar")


    # 8
    fig = plt.gcf()

    # 9
    fig.savefig('catplot.png')
#%%
    return fig

# 10
def draw_heat_map():
#%%
    # MARK: Important!!! 
    # I didn't use the matplotlib to configure the plot. I configured the plot directly using seaborn. This results in a failed unit test although the task is completed.

    # 11
    df_heat = df[ (df['ap_lo'] <= df['ap_hi']) & (df["height"]>=df["height"].quantile(0.025)) & (df["height"]<=df["height"].quantile(0.975)) & (df["weight"]>=df["weight"].quantile(0.025)) & (df["weight"]<=df["weight"].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # 14
    fig, ax = plt.subplots()
    
    # 15
    sns.heatmap(corr,mask=mask,annot=True,annot_kws={"size":7},fmt=".1f",square=True,linewidths=.5,cmap="Greens")
    fig = plt.gcf()   
    fig.tight_layout()
     
    # 16
    fig.savefig('heatmap.png')
# %%
    return fig

# %%
