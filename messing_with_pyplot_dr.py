from matplotlib import pyplot as plt
from collections import Counter

"""
CREATING A LINE GRAPH
"""

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')

# add a title
plt.title("Nominal GDP")

# add labels to the axis
plt.ylabel("Billions of $")
plt.xlabel("Years")

plt.show()

"""
CREATING A BAR GRAPH
"""

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + .1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i + .5 for i, _ in enumerate(movies)], movies)

plt.show()

"""
CREATING A HISTOGRAM
"""
grades  = [83, 95, 91, 87, 70, 0 , 85, 82, 100, 67, 73, 77, 0]

# Lambda function that rounds a grade to the nearest tens
round_tens = lambda grade: grade // 10 * 10

# Creates a dict where each grade is the key and
# it's value is the Frequency of the grade
histogram = Counter(round_tens(grade) for grade in grades)

plt.bar([i - 4 for i in histogram.keys()],    # Offsets the x by 4
        histogram.values(),                    # Frequency of each grade
        8)                                      # Width of each bar

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

"""
LINE CHARTS
"""
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

# Sum of variance and bias
total_error = [x + y for x, y in zip(variance, bias_squared)]

# X-axis
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,      'g-',   label='variance') # green solid line
plt.plot(xs, bias_squared,  'r-.',  label='bias^2') # red dot-dashed line
plt.plot(xs, total_error,   'b:',   label='total error') # blue dotted line

# because we've assigned labels to each series # we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

"""
SCATTER PLOTS
"""
friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(   label,
                    xy=(friend_count, minute_count),    # put the label with its point
                    xytext=(5, -5),                     # but slightly offset
                    textcoords = 'offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()
