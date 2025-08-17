import matplotlib.pyplot as plt
import seaborn as sns

def city_sales_graph(df):
    sns.barplot(x="city", y="Income", data=df)
    plt.title("Ingresos por ciudad")
    plt.show()
