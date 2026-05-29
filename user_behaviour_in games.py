import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('online_gaming_behavior_dataset.csv')
print("Dataset loaded!", df.shape)
print(df[['Age','PlayTimeHours','AvgSessionDurationMinutes','PlayerLevel','AchievementsUnlocked']]
      .describe().round(2))

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("Gaming Behavior Analysis", fontsize=16, fontweight="bold")


axes[0, 0].hist(df["Age"], bins=15, color="steelblue")
axes[0, 0].set_title("Age Distribution")
axes[0, 0].set_xlabel("Age")
genre_avg = df.groupby("GameGenre")["PlayTimeHours"].mean().sort_values()
genre_avg.plot(kind="barh", ax=axes[0, 1], color="coral")
axes[0, 1].set_title("Avg Play Time by Genre")
axes[0, 1].set_xlabel("Hours")

df["EngagementLevel"].value_counts().plot(kind="pie", ax=axes[0, 2], autopct="%1.1f%%")
axes[0, 2].set_title("Engagement Levels")
axes[0, 2].set_ylabel("")

diff_avg = df.groupby("GameDifficulty")["SessionsPerWeek"].mean()
diff_avg.plot(kind="bar", ax=axes[1, 0], color="mediumseagreen", rot=0)
axes[1, 0].set_title("Sessions/Week by Difficulty")
axes[1, 0].set_ylabel("Sessions")


df.groupby("EngagementLevel")["AchievementsUnlocked"].mean().plot(kind="bar", ax=axes[1, 1], color="mediumpurple", rot=0)
axes[1, 1].set_title("Avg Achievements by Engagement")
axes[1, 1].set_ylabel("Achievements")

loc_avg = df.groupby("Location")["PlayTimeHours"].mean().sort_values()
loc_avg.plot(kind="barh", ax=axes[1, 2], color="goldenrod")
axes[1, 2].set_title("Avg Play Time by Location")
axes[1, 2].set_xlabel("Hours")

plt.tight_layout()
plt.savefig('gaming_behavior_analysis.png', dpi=150, bbox_inches="tight")
print("Chart saved!")
plt.show()