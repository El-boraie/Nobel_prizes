# 🏅 Nobel Prize Data Visualization Project with Seaborn

This project uses **Python**, **pandas**, and **Seaborn** to analyze and visualize key insights from a dataset of Nobel Prize winners. The goal is to explore gender trends, geographic dominance, and other historical patterns in the Nobel landscape.

## 📁 Dataset
The dataset used is `nobel.csv`, which contains records of Nobel laureates, including their names, gender, birth country, category, and year of award.

---

## 📌 Project Objectives & Questions

### 1. 🧑‍🤝‍🧑 Most Commonly Awarded Gender & Country
- **Goal:** Determine which gender received the most Nobel Prizes and which countries produced the most laureates.
- **Visuals:** 
  - Bar chart of gender counts.
  - Count plot of top 7 birth countries split by gender.

### 2. 🇺🇸 USA Dominance by Decade
- **Goal:** Identify which **decade** had the **highest ratio of US-born Nobel Prize winners** to all winners.
- **Approach:** 
  - Created a new `decade` column.
  - Calculated the mean ratio of US-born winners by decade.
- **Visuals:** 
  - Bar plot showing `us_ratio` by decade.

### 3. 👩‍🔬 Highest Female Laureate Proportions by Decade & Category
- **Goal:** Find the combination of decade and category with the **highest proportion of female laureates**.
- **Approach:** 
  - Created an `is_female` boolean column.
  - Grouped by `decade` and `category` to calculate female proportions.
- **Visuals:** 
  - Horizontal bar plot with hue for each decade showing female proportions by category.

### 4. 🥇 First Female Nobel Laureate
- **Goal:** Identify the **first woman** to win a Nobel Prize and in which category.
- **Method:**
  - Filtered by gender, selected the earliest year entry.
  - Extracted name and category.

### 5. 🔁 Repeat Winners
- **Goal:** Determine individuals or organizations who have won **more than once**.
- **Approach:** 
  - Counted occurrences of full names.
  - Filtered names with counts ≥ 2.
- **Output:** 
  - List of repeat laureates along with their award years, types, and categories.

---

## 📊 Libraries Used
- [`pandas`](https://pandas.pydata.org/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`matplotlib`](https://matplotlib.org/)
- `numpy`

---

💡 Key Insights
- Males have historically dominated Nobel Prizes.
- The highest ratio of US-born Nobel Prize winners to total winners in all categories was in 2000s in with a ratio of 0.42
- The highest proportion of female laureates with decade and category proportion was in 2020 in Literature with a ratio of estimate 4.95
- **Marie Curie née Sklodowska** was the first woman to receive a Nobel Prize — in Physics.
- A 8 individuals and 5 organizations have achieved the rare feat of winning multiple Nobel Prizes.

---
