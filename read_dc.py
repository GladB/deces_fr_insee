import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def format_data(dc):
    dc.columns = ["YYYY-MM", "nb_dc", "other"]
    dc.sort_values("YYYY-MM", inplace=True)
    return dc

def compute_date_columns(dc):
    dc["year"] = dc["YYYY-MM"].str[:4]
    dc["month"] = dc["YYYY-MM"].str[-2:]
    return dc

def compute_mean_columns(dc):
    dc['yearly_rolling_mean_dc'] = dc['nb_dc'].rolling(12).mean()
    return dc

def plot_deces(dc):
    sns.lineplot(data=dc, x="YYYY-MM", y="nb_dc")
    a = sns.lineplot(data=dc, x="YYYY-MM", y="yearly_rolling_mean_dc")
    a.set_xticks(range(0, len(dc)-1, 12))
    plt.xticks(rotation=45)
    # a.set_xticklabels(a.get_xticklabels(), rotation=45)
    plt.show()


if __name__ == "__main__":
    dc = pd.read_csv("./deces_annee_mois.csv", skiprows=4, header=None, sep=";")
    print(dc.head())
    dc = format_data(dc)
    dc = compute_date_columns(dc)
    dc = compute_mean_columns(dc)
    print(dc.head())

    # plot_deces(dc)

    dc_january = dc[dc.month.isin(["01", "06"])]
    print(dc_january.head())
    a = sns.barplot(data=dc_january, x="year", y="nb_dc", hue="month")
    plt.xticks(rotation=90)
    plt.show()

    