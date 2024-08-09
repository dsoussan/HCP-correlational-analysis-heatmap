from scipy.stats import pearsonr
import pandas as pd
from prettytable import PrettyTable

### Gather Data ###
# Read the Excel file (replace 'sample.xlsx' with your file path)
df = pd.read_excel('Master.xlsx', sheet_name='')

# Display the DataFrame
print(df)

### Calculate Pearson Correlations ###
# Example data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Calculate Pearson correlation
corr, p_value = pearsonr(x, y)
print(f'Pearson correlation: {corr}, P-value: {p_value}')

from scipy.stats import pearsonr

# Assuming you have arrays x and y
correlation_coefficient, p_value = pearsonr(x, y)
print(f"Pearson correlation coefficient: {correlation_coefficient:.4f}")
print(f"P-value: {p_value:.4f}")


### Create md format Table ###
# Change this to include the correct data

myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])
myTable.add_row(["Leanord", "X", "B", "91.2 %"])
myTable.add_row(["Penny", "X", "C", "63.5 %"])

# Add more rows as needed

print(myTable)