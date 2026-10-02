import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Python": [90, 77, 100, 88, 92],
    "SQL": [78, 88, 91, 84, 89],
    "React": [90, 80, 89, 92, 94]
}

df = pd.DataFrame(data)

sns.pairplot(df)

plt.show()