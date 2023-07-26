import csv

def count_content_in_categories(filename):
    # Create a dictionary to store the count of content in each category
    category_count = {}

    # Open the CSV file and read its contents
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            categories = row['listed_in'].split(', ')  # Split multiple categories if any
            for category in categories:
                category_count[category] = category_count.get(category, 0) + 1

    return category_count

if __name__ == "__main__":
    filename = "netflix_data.csv"
    category_count = count_content_in_categories(filename)

    for category, count in category_count.items():
        print(f"{category}: {count}")
