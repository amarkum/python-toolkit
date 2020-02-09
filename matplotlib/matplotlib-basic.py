from matplotlib import pyplot as plt

# plot an X vs Y graph
# the X array length must be equal to Y array length
plt.plot([1, 2, 3, 4, 5, 6], [56, 60, 35, 50, 85, 100])

# add the title, x-axis and y-axis label
plt.title('Marks of Student')
plt.xlabel('roll number of student')
plt.ylabel('marks obtained')

# shows us the plotted graph
plt.show()

