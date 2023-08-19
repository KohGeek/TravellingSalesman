# take the average of each of the key of json file
# input: json file

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.preprocessing import OrdinalEncoder

def read_json(json_file):
    # read json file
    # convert to dataframe
    with open(json_file) as f:
        data = json.load(f)

    df = pd.DataFrame()

    for key in data:
        for value in data[key]:
            df = pd.concat([df, pd.DataFrame({"key": [key], "value": [value]})])
            df.reset_index(drop=True, inplace=True)

            # set both column as float
            try:
                df["key"] = df["key"].astype(float)
            except:
                df["key"] = df["key"].astype(str)
            df["value"] = df["value"].astype(float)

            enc = OrdinalEncoder()
            df["encode"] = enc.fit_transform(df[["key"]])
                
    #print full df
    print(df)
    return df

def plot(data, x_label):
    sns.set(style="darkgrid")

    x = data["encode"]
    y = data["value"]

    ax = sns.boxplot(x="key", y=y, data=data)
    if data.key.dtype == "float64":
        ax = sns.regplot(x=x, y=y, data=data, order=2, truncate=False, scatter=False)
    ax.set(xlabel=x_label, ylabel="Best Distance")

    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig("plots/" + x_label + ".png")
    plt.show()

    # export the plot to png

if __name__ == "__main__":
    filename = "pops"

    jsondata = read_json("jsons/" + filename + ".json")
    plot(jsondata, filename)
