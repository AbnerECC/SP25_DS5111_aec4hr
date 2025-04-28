import os
import pandas as pd

# Path to the folder containing your CSV files
folder_path = "/home/ubuntu/SP25_DS5111_aec4hr/bin/normalized_gainers/"

# List to store data from each file
data_frames = []

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):  # Only process CSV files
        file_path = os.path.join(folder_path, file_name)
        # Read the CSV file and append to the list
        data_frames.append(pd.read_csv(file_path))

# Combine all dataframes into one
full_data = pd.concat(data_frames, ignore_index=True)

# Save the combined dataframe to a new CSV file
full_data.to_csv("numbers.csv", index=False)
print("All files have been combined into 'full_combined.csv'")