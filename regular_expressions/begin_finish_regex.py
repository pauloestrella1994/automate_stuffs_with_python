import re

#Match the object only with it's in the begging of the string (^)
beginRegex = re.compile(r'^Hello')
mo = beginRegex.search('Hello there!')
mo2 = beginRegex.search('He said "Hello"')
print(mo.group())

if not mo2:
    print("Can't match object")


#find the object in the final of the string ($)
endRegex = re.compile('world!$')
mo = endRegex.search('Hello world!')
print(mo.group())

#find all digits in the regex pattern in a string, beginning with ^, ending with $
alldigitsRegex = re.compile(r'^\d+$')
mo = alldigitsRegex.search('7851498645929546')
print(mo.group())

#find any caractere plus the pattern with .
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat!')
print(mo)

#find any object after a specify string, using . and * for multiples objects
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall('First Name: Paulo Last Name: Netto')
print(mo)

#matching in two different ways the pattern between marks
serve = '<To serve humans> for dinner>'

firstmarkRegex = re.compile(r'<(.*?)>')
lastmarkRegex = re.compile(r'<(.*)>')

print(firstmarkRegex.findall(serve))
print(lastmarkRegex.findall(serve))

#the expression .* find all objects, except a new line. To find all the strings, even if it has lines, set re.DOTALL in compile
phrase = " Hello\n Beautiful\n World"
dotAllRegex = re.compile(r'.*', re.DOTALL)
mo = dotAllRegex.search(phrase)
print(mo.group())

#to match any characteres, upper or lower case, set in compile r.I
phrase = 'WhY PROgrAmminG Is so HArD?'
lowerupperRegex = re.compile(r'[aeiou]', re.I)
print(lowerupperRegex.findall(phrase))