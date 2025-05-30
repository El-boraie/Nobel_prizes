# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

nb = pd.read_csv("data/nobel.csv")
print(nb.columns)
nb

#-----------------------------------------------------------------------------------------------------------
# Question 1
# What is the most commonly awarded gender?
gender_count = nb["sex"].value_counts()

s = sns.catplot(x="sex", 
                data=nb, 
                kind="count", 
                hue="sex")
s.fig.suptitle("Noble Prizes Count for Each Gender")

top_gender = nb["sex"].value_counts().idxmax()

# What is the most commonly awarded birth country?
top = nb["birth_country"].value_counts().head(7).index

top7_countries = nb[nb["birth_country"].isin(top)]

c = sns.catplot(y="birth_country", 
                hue="sex", 
                data=top7_countries, 
                kind="count", 
                col="sex", 
                sharex=False)

c.fig.suptitle("Noble Prizes for Top 7 Counties", y=1.05)

top_country = nb["birth_country"].value_counts().idxmax()

plt.show()

#-----------------------------------------------------------------------------------------------------------
# Question 2
# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?

# Creating the "decade" column
nb["decade"] = (nb["year"] // 10) * 10

nb["is_USA"] = nb["birth_country"] == "United States of America"
decade_ratios = nb.groupby("decade", as_index=False)["is_USA"].mean()
decade_ratios.rename(columns={"is_USA": "us_ratio"}, inplace=True)

# Barplot for the ratio
sns.barplot(x="decade", 
            y="us_ratio", 
            data=decade_ratios, 
            color="skyblue", 
            edgecolor="black")

# Title and labels
plt.title("Ratio of US-born Nobel Prize Winners by Decade", y=1.05)
plt.xlabel("Decade")
plt.ylabel("Ratio of US-born Winners")
plt.xticks(rotation=45)
plt.show()

# The decade had the highest ratio of US-born Nobel
max_decade_usa = decade_ratios.loc[decade_ratios["us_ratio"].idxmax(), "decade"]
print(max_decade_usa)

#-----------------------------------------------------------------------------------------------------------
# Question 3
# Which decade and Nobel Prize category combination had the highest proportion of female laureates?

# Creating the "is_female" column
nb["is_female"] = nb["sex"] == "Female"

# Group by to calculate the proportion of female winners by decade and category
female_proportions = nb.groupby(["decade", "category"])["is_female"].mean()

max_female_combination = female_proportions.idxmax() 

# Step 4: Create the dictionary
max_female_dict = {
    max_female_combination[0]: max_female_combination[1] 
}

# Reseting index
female_proportions_reset = female_proportions.reset_index()

# Barplot
f = sns.barplot(
    data=female_proportions_reset,
    x="is_female",
    y="category",
    hue="decade",
    palette="viridis"
)

# Add labels and title
plt.title("Proportion of Female Laureates by Decade and Category")
f.set(xlabel="Proportion of Female Laureates", 
      ylabel="Category")

plt.show()

#-----------------------------------------------------------------------------------------------------------
# Question 4
# Who was the first woman to receive a Nobel Prize, and in what category?
women = nb[nb["sex"] == "Female"]
women

# First women ever to win a Nobel prize
first_women = women.loc[women["year"].idxmin()]
first_women

# First women's full name to win a Nobel prize 
first_woman_name = first_women["full_name"]
first_woman_name

# First women's category in a Nobel prize 
first_woman_category = first_women["category"]
first_woman_category

#-----------------------------------------------------------------------------------------------------------
# Question 5
# Which individuals or organizations have won more than one Nobel Prize throughout the years?
value_count = nb["full_name"].value_counts()

repeats = value_count[value_count >= 2].index

repeated_winners = nb[nb["full_name"].isin(repeated_win.index)]

repeated_winners = repeated_winners[["full_name", "year", "laureate_type", "category"]]

repeat_list = list(repeats)

print(repeat_list)
repeated_winners

#-----------------------------------------------------------------------------------------------------------