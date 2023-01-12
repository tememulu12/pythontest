import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv")
print(df)
df['data'] = pd.to_datetime(df.date, format='%d/%m/%Y')
x = df['data']
y = df['Close']
# figura, ax = plt.subplots(figsize=(10, 4))
# ax.scatter(x, y, marker='*', alpha=.5)
lista = [100, 1999]

figura, ax = plt.subplots(2, figsize=(10, 4))
ax[0].scatter(x, y, marker='+', alpha=.5)
_ = ax[1].pie(lista, labels=['wpłata', 'wypłata'])
# _ = ax.legend()
plt.show()


plt.show()
