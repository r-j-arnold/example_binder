import csv
import numpy as np
import scipy.stats

# Read in the data
with open('data.csv') as data_file:

    reader = csv.reader(data_file)
    headers = next(reader)
    data = list(reader)
    data=np.array(data).astype(float).T

x = data[0]
y = data[1]

# Do linear regression and print the results
print(scipy.stats.linregress(x, y))




