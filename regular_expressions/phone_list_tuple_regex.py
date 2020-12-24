import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-1012'

#findall method will result in a list of match objects, but, if it has any group in mo, the return wil be a list of tuples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo_list = phoneNumRegex.findall(message)
print(mo_list)

#to find a list of tuples and the entire object, put some parentheses
phoneNumRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo_list = phoneNumRegex.findall(message)
print(mo_list)

#find inside a lyric some pattern, \d+ for one or more digits, \s for a space and \w+ for one or more characteres
lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing,
            8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 
            4 calling birds, 3 french hens,
            2 turtle doves and a partridge in a pear tree walk into a bar '''
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

#find specifics letters in lower or upper case
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))

#find specifics letters in lower or upper case double time
doublevowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doublevowelRegex.findall('Robocop eats baby food'))

#find characteres that are not in the list, adding ^
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))