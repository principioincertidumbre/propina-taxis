import matplotlib.pyplot as plt
import seaborn as sns

def lineplot(df,x,y,xlabel, ylabel, label):
    sns.lineplot(data=df, x=x, y=y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(label, loc='center')
    plt.show()
    return
