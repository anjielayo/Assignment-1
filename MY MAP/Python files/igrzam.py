import numpy as np
from matplotlib import pyplot as plt


dev_x=['Q1 (JAN-MAR)','Q2 (APR-JUN)','HALF YEAR TOTAL']
dev_y=[3.57,3.52,7.09]
plt.bar(dev_x, dev_y, color='#f0f00c')

#plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for Zamfara State')
plt.xlabel('Months of the Year')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
