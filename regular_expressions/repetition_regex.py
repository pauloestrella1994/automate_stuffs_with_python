import re

#find words that a specify sufixes, into the parentheses and before "?", can appear zero or one time
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventures of Batwoman')
print(mo.group())
print(mo2.group())

#find words that a specify sufixes, into the parentheses and before "*", can appear zero or more times
batRegex2 = re.compile(r'Bat(wo)*man')
mo3 = batRegex2.search('The adventures of Batman')
mo4 = batRegex2.search('The adventures of Batwowowowoman')
print(mo3.group())
print(mo4.group())

#find words that a specify sufixes, into the parentheses and before "+", can appear one or more times
batRegex3 = re.compile(r'Bat(wo)+man')
mo5 = batRegex3.search('The adventures of Batwoman')
mo6 = batRegex3.search('The adventures of Batwowowowoman')
print(mo5.group())
print(mo6.group())

#find litteraly the objects +*? with "\"
regex = re.compile(r'\+\*\?')
mo7 = regex.search("I learned about +*? regex syntax")
print(mo7.group())

#also find litteraly the objects +*? with "\" in a group with +
regex2 = re.compile(r'(\+\*\?)+')
mo8 = regex2.search("I learned about +*?+*?+*?+*?+*? regex syntax")
print(mo8.group())

#find a specific number of sufixes repetitions
haRegex = re.compile(r'(Ha){3}')
mo9 = haRegex.search('He said "HaHaHa"')
print(mo9.group())

#example using regex to find phone numbers three times
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo10 = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo10.group())

#find a specific range of sufixes repetitions {min, max}
haRegex2 = re.compile(r'(Ha){3,5}')
mo11 = haRegex2.search('He said "HaHaHa"')
mo12 = haRegex2.search('He said "HaHaHaHaHa"')
print(mo11.group())
print(mo12.group())