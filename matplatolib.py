import matplotlib.pyplot as plt
import numpy as np

# plot - numbers
print("MatPlotLib python file")
plt.plot([1,2,3], [4,5,6])
plt.xlabel("Random Numbers set 1")
plt.ylabel("Random Numbers set 2")
plt.show()

# plot -runs vs years
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

plt.plot(years, runs)
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Sachin Tendulkar's Yearly Runs")
plt.show()

# plot- multiple lines

Kapil = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
John = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
plt.plot(years, John, label="John")
plt.plot(years, Kapil, label="Kapil")

plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.legend()
plt.show()

# 

for i in range(5):
    plt.plot(np.random.rand(10), linewidth=1)

plt.title("Too Much Data!")
plt.grid(True)
plt.tight_layout()
plt.show()

# style for lines
plt.plot(years, John, 'ro--', label="John")  
plt.plot(years, Kapil, 'g^:', label="Kapil")  
plt.legend()
plt.show()