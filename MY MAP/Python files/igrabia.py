import numpy as np
from matplotlib import pyplot as plt


dev_x=['Q1 (JAN-MAR)','Q2 (APR-JUN)','HALF YEAR TOTAL']
dev_y=[4.27,1.92,6.19]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#0f0f0fbd')

#plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for Abia State')
plt.xlabel('Months of the Year')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
