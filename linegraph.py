import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x='Average_Pulse', y='Calorie_Burnage',kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()

plt.savefig(sys.stdout.buffer)