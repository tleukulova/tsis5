#first solving way
import re
txt = input()
pattern = r'ab*'
match = re.search(pattern, txt)
if match:
    print("yes")
else:
    print("no")

#second solving way
import re

txt = "abb ab a"

x = re.findall("a{1}d*", txt)
print (x)