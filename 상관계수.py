import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('#결과.csv')

df = df.drop('업종', axis = 1)

corr_matrix = df.corr(method='spearman')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    linewidths=0.5,
    vmin=-1, vmax=1
)

plt.title('상관계수', fontsize=16, pad=20)
plt.tight_layout()
plt.show()