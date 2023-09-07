# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
#
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
#
# Good Luck!


def double_char(string):
	result = ''
	for character in string:
		result += character * 2
	return result
