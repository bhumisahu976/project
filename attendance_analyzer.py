import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Name': ['Arjun', 'Priya', 'Rohan', 'Sneha', 'Vikram', 'Anjali', 'Kabir', 'Meera'],
    'Attended': [45, 20, 38, 48, 15, 30, 42, 25],
    'Total': 50
})

df['Pct'] = (df['Attended'] / df['Total'] * 100).round(2)

df['Category'] = pd.cut(
    df['Pct'], 
    bins=[0, 60, 75, 101], 
    labels=['Poor', 'Average', 'Good'], 
    right=False
)

print(df)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

bar_colors = ['green' if x >= 75 else 'orange' if x >= 60 else 'red' for x in df['Pct']]

ax1.bar(df['Name'], df['Pct'], color=bar_colors)
ax1.set_title("Student Attendance %")
ax1.set_ylim(0, 100)

df['Category'].value_counts().plot.pie(
    ax=ax2, 
    autopct='%1.1f%%', 
    colors=['lightcoral', 'gold', 'lightgreen'],
    ylabel=''
)
ax2.set_title("Category Distribution")

plt.tight_layout()
plt.show()
