##Assignements..Data analysis and visualization.


# Create a DataFrame with 5 students’ names, ages, and marks.
# Print only those who scored above 80.

import pandas as pd
listing = { "Name": ["Amna", "sara", "Afreen", "Arshin", "Hafsa"]
           ,"ages": [21, 22, 81, 76, 87],
           "marks": [32, 48, 90, 85, 78]}
df = pd.DataFrame(listing)
print(df[df["marks"]>80])
##Done

# Load data from a CSV file named sales.csv.
# Display only the first 10 records.
df = pd.read_csv("sales.csv")
print(df.head(10))
###Done

# Remove missing and duplicate records from the data.
data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Ali', 'Fatima', None, 'Ahmed', 'Bilal', 'Bilal'],
    'Age': [25, 30, None, 25, 28, 22, None, 40, 40],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', None, 'Peshawar', 'Islamabad', 'Quetta', None],
    'Score': [85, 90, 78, 85, 92, 70, 78, None, None]
}
df = pd.DataFrame(data)

print("🔹 Original Data:")
print(df)

df_cleaned = df.drop_duplicates()
print(df_cleaned)

###done


# # Rename columns: “Revenue” → “Sales_Amount” and “Profit” → “Net_Profit”.
data=  ({"region": [ "desert", "watery", "dusty"],
                   "Revenue": [ 32, 56, 76],
                     "Profit": [ 12, 23, 34]
                     })

df = pd.DataFrame(data)
df.rename(columns={'Revenue': 'Sales_Amount', 'Profit': 'Net_Profit'}, inplace=True)

print("\nAfter renaming:")
print(df)

###Done.

# Group sales data by “Region” and calculate average “Sales_Amount”.
progress = {"Region":["Desert", "watery", "dusty"],
            "Sales_Amount": [ 32, 56, 76]}

grouped = progress.groupby("Region")["Sales_Amount"].mean()
print(grouped)
###Done
