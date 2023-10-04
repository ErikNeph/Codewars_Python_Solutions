# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.


def find_average(array):
	return sum(array) / len(array) if array else 0
