import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x*x*x for x in x_values]

plt.style.use('seaborn-paper')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

plt.show()