# Given a string of digits, you should replace any digit below
# 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string


def fake_bin(number_string):
	binary_string = ""
	for num in number_string:
		if int(num) < 5:
			binary_string += "0"
		else:
			binary_string += "1"
	return binary_string
