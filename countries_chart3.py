import pandas as pd

# Read the CSV file
df = pd.read_csv('netflix_data.csv')

# Create separate dataframes for TV Shows and Movies
df_tvshows = df[df['type'] == 'TV Show']
df_movies = df[df['type'] == 'Movie']

# Get the count of TV Shows and Movies per country
tvshows_per_country = df_tvshows['country'].value_counts()
movies_per_country = df_movies['country'].value_counts()

# Combine these counts into a single dataframe
combined = pd.concat([tvshows_per_country, movies_per_country], axis=1)
combined.columns = ['TV Shows', 'Movies']

# Create a total column
combined['Total'] = combined.sum(axis=1)

# Sort by the total column in descending order
combined = combined.sort_values('Total', ascending=False)

# Print the top 10
print(combined.head(10))

