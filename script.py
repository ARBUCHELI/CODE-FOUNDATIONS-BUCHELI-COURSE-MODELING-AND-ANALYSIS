import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Paste code for scatter plot:
x = new_df["population_proper"]
y = new_df["age"]
 
plt.scatter(x, y, alpha=0.5)

# Paste code for linear regression:
sns.regplot(x="population_proper", y="age", data=new_df)

# Show plot
plt.show()

