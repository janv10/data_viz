import pandas as pd

# Assuming your data is in a CSV file named "netflix_data.csv"
# Adjust the file path if necessary
file_path = "netflix_data.csv"

# Load the data into a pandas DataFrame
df = pd.read_csv(file_path)

# Get the "listed_in" column
listed_in_column = df["listed_in"]

# Create a list to store dictionaries for each category
category_list = []

# Iterate through each row in the "listed_in" column
for categories in listed_in_column:
    # Split the comma-separated categories in the current row
    category_list_split = categories.split(", ")
    
    # Count the occurrences of each category
    for category in category_list_split:
        category = category.strip()  # Remove any leading/trailing spaces
        # Check if the category already exists in the list
        existing_category = next((item for item in category_list if item["category"] == category), None)
        if existing_category:
            existing_category["count"] += 1
        else:
            category_list.append({"category": category, "count": 1})

# Print the category names and their occurrences in the desired format
for category_info in category_list:
    print(f"{category_info}")
