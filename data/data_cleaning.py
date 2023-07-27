import pandas as pd


file_path = "netflix_data.csv"

df = pd.read_csv(file_path)
listed_in_column = df["listed_in"]
category_list = []

for categories in listed_in_column:
    category_list_split = categories.split(", ")
    
    for category in category_list_split:
        category = category.strip() 
        existing_category = next((item for item in category_list if item["category"] == category), None)
        if existing_category: existing_category["count"] += 1
        else: category_list.append({"category": category, "count": 1})

for category_info in category_list:
    print(f"{category_info}")
