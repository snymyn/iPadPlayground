import webbrowser, sys

# webbrowser.open("http://theselftaughtprogrammer.io")
"""
i = 0
while i < 100:
	print("Hello!")
	i += 1
	
"""

# Regular expressions --> re
"""
import re

l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

line = "123 hi 34 hello"
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
	print(match)
	

"""

## Mad Libs Game
text = "Hey this is __Name__. And Do you know who you __You__ are?"

import re
def mad_libs(mls):
	hints = re.findall("__.*?__", mls)
	if hints is not None:
		for word in hints:
			q = "input {}:".format(word)
			new = input(q)
			mls = mls.replace(word, new, 1)
		print("\n")
		mls = mls.replace("\n", "")
		print(mls)
	else:
		print("Argument mls is invalid")
mad_libs(text)
