import seaborn as sns
import matplotlib.pyplot as plt
# Load example dataset
tips = sns.load_dataset("tips")
# Scatter plot of total bill vs tip
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="sex", size="size")
plt.title("Tips Scatter Plot")
plt.show()