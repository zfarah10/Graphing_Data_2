"""
Program Name: Lab15_zfarah_1.py
Author: Zakarie Farah
Purpose: Read unemployment rate data from a CSV file and make a simple line graph.
Date: 8/7/2025
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# file name with the unemployment data
filename = "OHUR.csv"

dates = []
rates = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # just to see what the columns are
    for i, col in enumerate(header_row):
        print(i, col)

    # read the data from each row
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
        except ValueError:
            # skip rows with bad/missing data
            continue
        else:
            dates.append(date)
            rates.append(rate)

# make the graph
plt.figure(figsize=(10, 5))
plt.plot(dates, rates, color='blue', linewidth=1.5)

# add titles and labels
plt.title("US Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

# make the x-axis labels fit better
plt.tight_layout()
plt.show()
