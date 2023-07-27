import pandas as pd

df = pd.read_csv('netflix_data.csv')

df_tvshows = df[df['type'] == 'TV Show']
df_movies = df[df['type'] == 'Movie']

tvshows_per_country = df_tvshows['country'].value_counts()
movies_per_country = df_movies['country'].value_counts()

combined = pd.concat([tvshows_per_country, movies_per_country], axis=1)
combined.columns = ['TV Shows', 'Movies']
combined['Total'] = combined.sum(axis=1)
combined = combined.sort_values('Total', ascending=False)
print(combined.head(10))

