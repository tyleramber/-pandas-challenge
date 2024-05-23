import os
import csv

input_path = os.path.join("PyBank","Resources", "budget_data.csv")

rows = []
with open(input_path, encoding="utf-8") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

months = []
profit_losses = []


for row in rows:
    months.append(row[0])
    profit_losses.append(int(row[1]))

# Calculate the total number of months
TOTAL_DATE = len(months)

# Calculate the net total amount of profit/losses
net_total = sum(profit_losses)

# Calculate the changes in profit/loss over the entire period
changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]

# Calculate the average of changes
average_change = sum(changes) / len(changes)

# Calculate the greatest increase in profits and corresponding month
max_increase = max(changes)
max_increase_index = changes.index(max_increase)
max_increase_month = months[max_increase_index + 1]

# Calculate the greatest decrease in profits and corresponding month
max_decrease = min(changes)
max_decrease_index = changes.index(max_decrease)
max_decrease_month = months[max_decrease_index + 1]
# Create the financial analysis report text
report = (
    f"{' Financial Analysis ':-^48}\n"
    f"{'Total Months:':24}{TOTAL_DATE:24,.0f}\n"
    f"{'Total:':24}{net_total:24,.0f}\n"
    f"{'Avg Change:':24}{average_change:24.0f}\n"
    f"{'Greatest Increase in Profits:':10}{max_increase_month:}{max_increase:14,.0f}\n"
    f"{'Greatest Decrease in Profits:':10}{max_decrease_month:}{max_decrease:14,.0f}\n"
    f"{'--':-^48}"
)
print (report)
# Assemble the output text file path, starting from the cwd
output_path = os.path.join("PyBank", "Analysis", "budget_analysis.txt")

# Open the budget_analysis text file and write the report to it
with open(output_path, "w", encoding="utf-8") as textfile:
    textfile.write(report)