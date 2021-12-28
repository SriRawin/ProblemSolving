import re
haystack = "hello"
needle = "ll"
result = re.search(needle, haystack).start()
print(result)
