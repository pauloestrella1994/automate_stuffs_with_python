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