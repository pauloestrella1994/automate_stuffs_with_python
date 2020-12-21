import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-1012'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

list_numbers = phoneNumRegex.findall(message)
print(list_numbers)