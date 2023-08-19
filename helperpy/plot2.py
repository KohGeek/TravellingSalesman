from functools import partial

import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def read_csv(csv_file):
    # read csv file
    # convert to dataframe
    df = pd.read_csv(csv_file, index_col=0)
    print(df)

    return df

def plot(data):

    sns.set(style="darkgrid")
    plt.figure(figsize=(8, 4.5))
    sns.lineplot(data=data, markers=False, dashes=True)

    
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig("plots/all.png")
    plt.show()

if __name__ == "__main__":
    csvdata = read_csv("all.csv")
    plot(csvdata)