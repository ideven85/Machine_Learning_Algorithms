# import the regular expression module
import re

# input string
string = "The roots of education are bitter, but the fruit is sweet."

# write a regular expression pattern to check if 'education' is present in a given string or not.
pattern = "education"

# store the match of regex
result = re.search(pattern, string)

# store the end of the match using result.end()
end_position = result.start()

# evaluate result - don't change the following piece of code, it is used to evaluate your regex
print(end_position)
