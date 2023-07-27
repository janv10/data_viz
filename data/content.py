import pandas as pd

data = pd.read_csv("netflix_data.csv")
country_counts = data.groupby("country")["type"].value_counts().unstack().fillna(0)

country_counts["Total_Content"] = country_counts["Movie"] + country_counts["TV Show"]

sorted_country_counts = country_counts.sort_values("Total_Content", ascending=False)

top_10_countries = sorted_country_counts.head(10)

print("Top 10 Countries with the Most TV Shows and Movies:")
print(top_10_countries[["Movie", "TV Show", "Total_Content"]])
