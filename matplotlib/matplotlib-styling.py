from matplotlib import pyplot as plt
from matplotlib import style

# call the ggplot style
style.use('ggplot')

x1 = [2008, 2009, 2010, 2011, 2012, 2013, 2014]
y1 = [53, 61, 77, 65, 75, 60, 90]

y2 = [134, 90, 95, 80, 77, 65, 80]

# plot two line, put in the label, add the width
plt.plot(x1, y1, 'g', label='Maruti', linewidth=2)
plt.plot(x1, y2, 'c', label='Hyudai', linewidth=2)

# add the legend to the graph which shows up the label of the line
plt.legend()

# add grid to the matplotlib
plt.grid(True, color='k')

# add up the title, xlabel and ylabel
plt.title('Car Sales in India')
plt.xlabel('Year')
plt.ylabel('Sales in Million')

# show the graph
plt.show()
