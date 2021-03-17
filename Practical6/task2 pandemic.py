import matplotlib.pyplot as plt
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
cases = [29862124, 11285561, 11205972, 4360823, 4234924]  # Input the data
explode = (0, 0, 0, 0, 0)  # make wedges attached to each other
plt.pie(cases, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=False, startangle=90)  # Define the chart
plt.axis('equal')  # ensure that it is a cirlce
plt.show()
