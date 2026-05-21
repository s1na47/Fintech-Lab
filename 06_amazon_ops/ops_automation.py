import pandas as pd

print("--- Starting Amazon Ops Automation ---")

# 1. Read the CSV file into a "DataFrame" (a virtual spreadsheet)
df = pd.read_csv('shift_data.csv')

# 2. Vectorized Math: Calculate Scans Per Hour for everyone instantly
df['Scans_Per_Hour'] = df['Packages_Scanned'] / df['Hours_Worked']

# 3. Filter: Find employees scanning less than 20 packages an hour
low_performers = df[df['Scans_Per_Hour'] < 20]

# 4. Export: Save the bad performers to a clean Excel report
low_performers.to_excel('Manager_Report.xlsx', index=False)

print("Report Generated: Manager_Report.xlsx")