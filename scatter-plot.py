import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Mohe', 'Karnal', 'Yrik', 'Jack'],
    'Age': [30, 21, 29, 28],
    'Weight': [70, 60, 75, 68]  # Added a 'Weight' column
}

df = pd.DataFrame(data)
sns.scatterplot(x='Age', y='Weight', data=df)
plt.show()
