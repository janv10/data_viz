import csv
from collections import defaultdict

def count_titles_by_year(filename):
    # Create dictionaries to store the counts for each year
    tv_shows_by_year = defaultdict(int)
    movies_by_year = defaultdict(int)

    # Open the CSV file and read its contents
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Extract the year from the date_added field
            try:
                year = int(row['date_added'].split(',')[-1].strip())
            except ValueError:
                # Print rows with invalid date format and skip them
                print(f"Invalid date format in row: {row}")
                continue

            # Check if it's a TV Show or Movie and update the counts accordingly
            if row['type'] == 'TV Show':
                tv_shows_by_year[year] += 1
            elif row['type'] == 'Movie':
                movies_by_year[year] += 1

    # Create a list of dictionaries in the desired format
    data = []
    for year in sorted(set(tv_shows_by_year.keys()) | set(movies_by_year.keys())):
        data.append({"year": year, "type": "TV Show", "count": tv_shows_by_year[year]})
        data.append({"year": year, "type": "Movie", "count": movies_by_year[year]})

    return data

if __name__ == "__main__":
    filename = "netflix.csv"
    data = count_titles_by_year(filename)

    print("const data2 = [")
    for entry in data:
        print(f'  {entry},')
    print("];")
