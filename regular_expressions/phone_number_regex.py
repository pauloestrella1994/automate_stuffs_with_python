import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-1012'

#find the phone number pattern
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

#find a list of numbers in string
list_numbers = phoneNumRegex.findall(message)
print(list_numbers)

#find a number and split into groups
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My phone is 444-444-4444')
print(mo2.group(1))
print(mo2.group(2))

#find string in parentheses
phoneNumRegex3 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo3 = phoneNumRegex3.search('My phone is (444) 444-4444')
print(mo3.group())

#find words with specify prefixes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo4 = batRegex.search('Batmobile lost a wheel')
print(mo4.group())

