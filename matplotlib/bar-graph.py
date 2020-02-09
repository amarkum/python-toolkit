from matplotlib import pyplot as plt

x1 = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y1 = [20, 55, 70, 75, 79, 85, 88, 92, 125]

y2 = [5, 28, 30, 35, 43, 56, 59, 74, 78]

# plot the bar
plt.bar(x1, y1, label='Population in India')
plt.bar(x1, y2, color='c', label='Population in US')

# add up the title, xlabel and ylabel
plt.title('Population Growth by Country')
plt.xlabel('Years')
plt.ylabel('Population in Million')

# add the legend, show the graph
plt.legend()
plt.show()
