"""
Module 2, Task 4
Student: Diandra O'Connor 1/19/23

Uses only Python Standard Library module:

Using statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
# vault scores
vault_scores = [
    9.4,
    9.6,
    9.85,
    9.55,
    9.0,
    9.8,
    9.2,
    8.85,
    9.7,
    9.75,
    9.45,
    9.4,
    9.8,
    9.7,
    9.85,
    9.1,
    9.45,
    9.6,
    9.65,
    9.35,
    9.55,
    9.65,
    8.5,
    9.3,
    9.15,
    9.0,
    9.6,
    9.65,
    9.55,
    9.8,
    9.7,
    9.7,
    9.4,
]



# Descriptive: averages and measures of central tendency:

mean = statistics.mean(vault_scores)
median = statistics.median(vault_scores)
mode = statistics.mode(vault_scores)

print()
print(f"A sample of vault scores was recorded as {vault_scores}")
print()
print(f"The mean vault score is {mean:.3f}")
print()
print(f"The median vault score is {median}")
print()
print(f"The mode for the vault scores is {mode}")
print()

# Descriptive: measure of spread

print()
print("To give us more information about how spread out the scores were")
print("we have a few more statistics below:")
print()

var = statistics.variance(vault_scores)
stdev = statistics.stdev(vault_scores)
lowest = min(vault_scores)
highest = max(vault_scores)


print(f"The variance is {var:.2f}")
print()
print(f"The standard deviation is {stdev:.2f}")
print()
print(f"The lowest vault score was {lowest} and the highest vault score was {highest}")
print()
print()

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
# x is number of hours of practice per week
# y is average all around score
x_practice_hours = [4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
y_avg_all_around_score = [33.5, 34, 34.3, 35, 35.4, 35.8, 36, 36.4, 36.7, 37.1, 37.3, 37.6]

xx_corr = statistics.correlation(x_practice_hours, x_practice_hours)
xy_corr = statistics.correlation(x_practice_hours, y_avg_all_around_score)

slope, intercept = statistics.linear_regression(x_practice_hours, y_avg_all_around_score)


# Choose an x value off in the future (future x)
# number of hours of practice per week
future_x = 22
future_xx = 24

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = (slope * future_x + intercept) # future/estimated all-around score
future_yy = (slope * future_xx + intercept) 

print(f"Here's some XY data: ")
print(f"The average number of practice hours is x: {x_practice_hours}")
print(f"The average all around score is y: {y_avg_all_around_score}")
print()
print(f"The correlation between x_practice_hours and x_practice_hours is {xx_corr:.2f}")
print(f"The correlation between x_practice_hours and y_avg_all_around_score is {xy_corr:.2f}")
print()
print()
print("Calculate the slope and intercept of the best fit line:")
print()
print(f"slope = {slope:.2f}") 
print(f"intercept = {intercept:.2f}")
print()
print(f"When x (number of practice hours per week) is 22,")
print(f"   y (average all around score) is predicted to be {future_y:.2f}")
print()
print(f"When x (number of practice hours per week is 24,")
print(f"   y (average all around score) is predicted to be {future_yy:.2f}")
print()

