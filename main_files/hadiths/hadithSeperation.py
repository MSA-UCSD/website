import pandas as pd

# Load the CSV file
df = pd.read_csv('all_hadiths_clean.csv')

# Filter the rows where column C has "Sahih Muslim" or "Sahih Bukhari"
filtered_df = df[df['source'].isin([' Sahih Bukhari ', ' Sahih Muslim '])]

# Save the filtered data to a new CSV file
filtered_df.to_csv('sahih_hadiths.csv', index=False)

print("Filtered data saved to 'sahih_hadiths.csv'.")
