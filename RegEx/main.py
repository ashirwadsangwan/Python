'''
Regular Expressions

“Knowing [regular expressions] can mean the difference between solving a problem in 3 steps and solving it
 in 3,000 steps. When you’re a nerd, you forget that the problems you solve with a couple keystrokes can 
 take other people days of tedious, error-prone work to slog through.”
'''
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

'''
The previous phone number–finding program works, but it uses a lot of code to do something limited: The 
isPhoneNumber() function is 17 lines but can find only one pattern of phone numbers. What about a phone 
number formatted like 415.555.4242 or (415) 555-4242? What if the phone number had an extension, like 
415-555-4242 x99? The isPhoneNumber() function would fail to validate them. You could add yet more code
for these additional patterns, but there is an easier way.
'''

'''
"\d" stands for a digit character in RegEx and the above function isPhoneNumber() can be replicated by looking
"\d\d\d-\d\d\d-\d\d\d\d" in the text file which says that it's looking for 3 digits followed by a hyphen then
3 digits and hyphen and then four digits.

We create a regex object by importing the library "re".
'''

import re

phoneNumRegEx = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

'''
Here, phoneNumRegEx contain a regex object.
'''
mo = phoneNumRegEx.search('My number is 415-555-4242.')
print("Phone number found : {}".format(mo.group()))

'''
Taking area codes away from the rest of the number. All we have to do is to put parantheses after the
area code and it'll create different groups when we'll search for it.
'''
regX = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
Number = regX.search('My number is 415-555-4242.')
print(Number.group(0))
print(Number.group(1)) # It represents the area code in the given phone number.
print(Number.group(2))
print(Number.group())

'''
If you want to retrieve the all the groups at once we can use the "groups" method.
'''
areaCode, mainNumber = Number.groups()
print(areaCode)
print(mainNumber)

'''
We can also use regex to match some other forms of patterns like suffix and prefixes.
'''
batRegex = re.compile(r'Bat(mobile|man|copter|bat)')
batty = batRegex.search("Batmobile lost a wheel")
print(batty.group())

'''
Sometimes you only want to match a pattern optionally.
'''
batReg = re.compile(r'Bat(wo)?man')
batty2 = batReg.search("They found Batman and Joker fighting.")
print(batty2.group())


'''
Matching zero or more with "*". The group that preceeds the star can occur any number of times in the text.
It can be completely be absent or repeated over and over again.
'''
batReg = re.compile(r'Bat(wo)*man')
batty3 = batReg.search('The adventures of Batman')
print(batty3.group())
batty4 = batReg.search("The adventures of Batwoman")
print(batty4.group())
batty5 = batReg.search("The adventures of Batwowowowowoman")
print(batty5.group())

'''
While "*" means zero or more matches, the "+" sign means one or more matches.
Unlike * which doesn't require its match to appear in the string for + you need to have present in the 
string at least once.

In string batty6 it won't match the string because you need at least one "wo" in the string and hence it
will return a None type object back.
'''
batReg = re.compile(r'Bat(wo)+man')
batty6 = batReg.search('The adventures of Batman')
print(batty6==None) # It represents that as woman doesn't appear in the string it will give None back.
batty7 = batReg.search("The adventures of Batwoman")
print(batty7.group())
batty8 = batReg.search("The adventures of Batwowowowowoman")
print(batty8.group())

'''
Matching specific repetitions with curly brackets.
'''
haRegex = re.compile(r'(Ha){3}')
ha1 = haRegex.search("HaHaHa")
print(ha1.group())
ha2 = haRegex.search("Ha")
print(ha2 == None)

'''
Greedy and Non-Greedy matching: 
Since (Ha){3,5} matches all 3, 4 and 5 occurances of Ha in a string.
The match object will return the longest match possible because it's greedy.

The non-Greedy way of doing this is putting a question mark after the curly bracket.
'''

greedyHaReg = re.compile(r'(Ha){3,5}')
ha3 = greedyHaReg.search("HaHaHaHaHa")
print(ha3.group())

nonGreedyHaReg = re.compile(r'(Ha){3,5}?')
ha4 = nonGreedyHaReg.search("HaHaHaHaHa")
print(ha4.group())

'''
In addition the Search method in the re module there's a method called findall as well. While the search
module returns the first instance of the search object while findall returns you all the matches find 
in the text document. 
findall returns all the results in the form of a list.
'''
phoneNumRegEx = re.compile(r'\d{3}-\d{3}-\d{4}')
num = phoneNumRegEx.search('Cell: 415-555-9999 Work: 212-555-0000')
print(num.group())
all_nums = phoneNumRegEx.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(all_nums)

'''
If there are groups in the regular expression then findall will return list of tuples. Each returned
tuple represents a found match, and its items are matched strings for each group in the regex.
'''
phoneNumRegEx = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
num = phoneNumRegEx.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(num)

'''
\d : any numeric that is 0-9.
\D : any numeric that is not 0-9.
\w : any letter, numeric digit or underscore character.(Think of this as matching word characters.)
\W : opposite of \w.
\s : any space, tab or newline(\n) character.
\S : opposite if \s.

In the below expression \d+ is searching for one or more digits followed by a space which is indicated by
\s and then one or more letter word. And findall returns you the list if all the instances that match.
'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

'''
Sometimes you want a specific result for which the shorthand character classes are too broad so you can make
your own class by using square brackets.
'''

vowelReg = re.compile(r'[aeiouAEIOU]')
print(vowelReg.findall("hello,homie. How are things on you End?"))

'''
We can also use ranges of classes using a hyphen b/w the ranges like [0-9a-zA-Z] which will look for
alphanumerics in an expression.
'''
consonantReg = re.compile(r'[^aeiouAEIOU]') # It's matching every chatacter that's not vowel.
print(consonantReg.findall("hello,homie. How are things on you End?"))

'''
You can also use the carrot sign (^) at the start of an expression to say that this match must occur at
the beginning of the text. And we use the ($) symbol at the end of the expression so that the match must
occur at the end of the text.
'''
startsWithHello = re.compile(r'^Hello')
hello = startsWithHello.search('Hello World!')
print(hello)

print(startsWithHello.search("he said, Hello")==None) # because it doesn't start with Hello.

endsWithNum = re.compile(r'\d$')
ends = endsWithNum.search("his age in 19")
print(ends)
print(endsWithNum.search('his age is 19 years.')==None)

'''
Now we can use the ($) to show if the whole string is number or not.
'''
wholeNum = re.compile(r'\d+$')
print(wholeNum.search('71818193292727'))
print(wholeNum.search('272727y828')) 
'''
In the string "272727y828" the string returned and which satisfies the condition is 828.
'''
wholeNum = re.compile(r'^\d+$')
print(wholeNum.search('71818193292727'))
print(wholeNum.search('272727y828')==None) 

'''
The (.) character on regular expression is called a wildcard and will match any character except for a
newline.
'''
atRegex = re.compile(r'.at')
print(atRegex.findall("The cat in the hat sat on the flat mat"))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
names = nameRegex.search("First Name: Sheldon Last Name: Cooper")
print(names.group())

'''
The dot star uses greedy mode. It tries to match as much text as possible.
'''
nonGreedReg = re.compile(r'<.*?>')
nonGreedy = nonGreedReg.search("<To serve man> for dinner>")
print(nonGreedy.group())

greedyReg = re.compile(r'<.*>')
greedy = greedyReg.search('<To serve man> for dinner>')
print(greedy.group())

'''
Case Insensitive Matching

Normally, regular expression match the text with the exact casing you specify. But sometimes all you
want is the same letters whether they are uppercase or lowercase it doesn't matter.
So, to do that we use an extra argument re.I which is for ignorecase.
'''
robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())

'''
Regular Expressions can't only find text but they can also substitute new text in place of the given text.
The sub() methods takes two arguments, first one is the text to be replaces and the second one is the new text
which will take that old place.

Sometimes you want to use some of the text for substitution from the given text itself. And we'll see an 
example below where we will hide the agent's name and just see the first letter.
'''
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub("CENSORED", 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesReg = re.compile(r'Agent (\w)\w*')
confidential = agentNamesReg.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(confidential)


'''
Managing Complex Regexes
'''
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)














