import pandas as pd

# Read the data from the CSV file
data = pd.read_csv("netflix_data.csv")

# Group the data by country and count the occurrences of TV shows and movies
country_counts = data.groupby("country")["type"].value_counts().unstack().fillna(0)

# Calculate the total number of contents (TV shows + movies) for each country
country_counts["Total_Content"] = country_counts["Movie"] + country_counts["TV Show"]

# Sort the data in descending order based on the total number of contents
sorted_country_counts = country_counts.sort_values("Total_Content", ascending=False)

# Get the top 10 countries with the most TV shows and movies
top_10_countries = sorted_country_counts.head(10)

# Display the results
print("Top 10 Countries with the Most TV Shows and Movies:")
print(top_10_countries[["Movie", "TV Show", "Total_Content"]])
