import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\ABHISHEK KUMAR\\Desktop\\iris (4).csv')

sns.pairplot(df,hue="Species")
plt.suptitle('Multivariate plot',y=1.02)
plt.show()


sns.boxplot(x='Species',y='sepal_length',data=df)
plt.title('Univariate plot')
plt.show()