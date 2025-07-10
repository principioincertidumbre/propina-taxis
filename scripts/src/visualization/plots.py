import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dataframe(list1,list2,list3):
    df = pd.DataFrame(list(zip(list1, list2, list3)),
         columns =['Mes', 'Cantidad ejemplos', 'F1-score'])
    return df

def lineplot(df,x,y, label):
    sns.lineplot(data=df, x=x, y=y)
    plt.title(label, loc='center')
    plt.show()
    return
