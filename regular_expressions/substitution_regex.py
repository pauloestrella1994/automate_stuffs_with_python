import re

#use the substitution method, sub()
nameRegex = re.compile(r'Agent \w+')
phrase = 'Agent Alice gave the secret document to Agent Bob'
subsNames = nameRegex.sub('CONFIDENCIAL AGENT', phrase)
print(subsNames)

#find the first letter (\1) of a name and set a character to hide the rest of the name
nameRegex = re.compile(r'Agent (\w)\w*')
hideNames = nameRegex.sub(r'Agent \1*****', phrase)
print(hideNames)

#Using re.VERBOSE, you can add lines and coomments to your regex, and also, combine methods with |
numberRegex = re.compile(
                    r'''\(\d\d\) #area code (with parenteses, no dash)
                    \s #space
                    \d\d\d\d  #no dash
                    - #dash between the number
                    \d\d\d\d''', re.IGNORECASE | re.VERBOSE)
phrase = 'My numbers are (99) 5555-5555 and (88) 5555-5555'
mo = numberRegex.findall(phrase)
print(mo)