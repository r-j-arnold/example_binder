import csv
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
with open('data.csv') as data_file:

    reader = csv.reader(data_file)
    headers = next(reader)
    data = list(reader)
    data=np.array(data).astype(float).T

x = data[0]
y = data[1]

#Plot the figure
plt.plot(range(1, 11), [i*2 for i in range(1, 11)], label='Model')
plt.scatter(x,y, label='Data', c='k')
plt.legend()
plt.show()
