from matplotlib import pyplot as plt
from collections import Counter
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2,543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# plt.plot(years, gdp, color="green", marker='o', linestyle="solid")

# plt.title("Nominal GDP")

# plt.ylabel("Billion$ of $$")
# plt.show()

# movies = ["Avengers", "Deadpool", "LOTR", "West Side Story", "Sound of Music"]

# num_oscars = [5, 11, 3, 8, 10]

# # bar width 0.8 by default, leaving 0.2 gap to the bar's right.
# # Hence have to + 0.1 to equalize this gap.
# xs = [i + 0.1 for i, _ in enumerate(movies)]

# plt.bar(xs, num_oscars)

# plt.ylabel("# of Academy Awards")
# plt.title("My fav things bahah")

# # i + 0.5 is the offset of the label
# plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

# plt.show()

# grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

# decile = lambda grade : grade // 10 * 10 # normalizes grades to nearest 10

# histogram = Counter(decile(grade) for grade in grades)

# plt.bar([x - 4 for x in histogram.keys()],
# 	histogram.values(),
# 	8) # histogram is a dictionary instantiated from an array of duplicate elements using Counter.

# plt.axis([-5, 105, 0, 5]) # x axis from -5 to 105 because of bar width 8, half width 4 giving padding
# # judiciously use .axis() because it's bad to set y origin to nonzero.
# # this is misleading and can lead to small margins seeming huge.

# plt.xticks([10 * i for i in range(11)]) # x : 0, 10, ... 100
# plt.xlabel("Decile")
# plt.ylabel('# students')
# plt.title('Dist of Exam grades')
# plt.show()

err1 = [1, 2, 5, 8, 4, 5, 9, 13]
err2 = [4, -2, 3, 4, 5, -1, 4, 11]
totalerr = [x + y for x, y in zip(err1, err2)]
xs = [i for i, _ in enumerate(err1)]

plt.plot(xs, err1, 'g:', label='err1')
plt.plot(xs, err2, 'r-.', label="err2")
plt.plot(xs, totalerr, 'b-', label='totalerr')

# creating the legend
plt.legend(loc=9) # code for 'top-center'
plt.xlabel('model complexity')
plt.title('err1 vs err2 vs totalerr')
plt.show()
