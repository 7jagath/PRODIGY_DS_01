import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv('Data.csv')

# 2. Create a Bar Chart for Gender
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Sex', palette='viridis')
plt.title('Distribution of Gender')
plt.show()

# 3. Create a Histogram for Age
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'].dropna(), bins=20, kde=True, color='teal')
plt.title('Age Distribution')
plt.show()
