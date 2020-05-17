#! python3
import re, pyperclip

#Todo: Create a regex for phone
phoneregex=re.compile(r'''
#123-123-1234 or (123)-123-1234 or (123) 123-1234
#or (123) 123-1234 ext 6789 or (123) 123-1234.ex6789 or (123) 123-1234 x6789
(((\d\d\d)|(\(\d\d\d\)))?        #area code (optional)
(\s|-)?                  #seperator
(\d\d\d)            #first three digits
(-)                  #seperator
(\d\d\d\d)          #last 4 digits
(\s)?
((ext(\.)?(\s)?|x)(\d{2,5}))?     #extension (optional)
)         #digits in extension           #digits in extension         
''', re.VERBOSE)
#Todo: Create a regex for email address
  #somet.+_hing@something.com
emailregex=re.compile(r'''
([a-zA-Z.+_0-9]+ #for name
@
[a-zA-Z.+_0-9]+) #for domain name
''', re.VERBOSE)

###We should find how he matches every individual phone to email using list concatenation
#Todo: Get the text from clipboard (read.pdf or ise pyperclip)
#read('/Users/hariaravi/Downloads/examplePhoneEmailDirectory.pdf')
text= pyperclip.paste()

#Todo: extract email and phone numbers
mophone=phoneregex.findall(text)
moemail=emailregex.findall(text)
justnumber=[] #since we expect the input to be from a list[tuplets]
for phonenumber in mophone:
    justnumber.append(phonenumber[0])

print(justnumber)
print(len(mophone))
print(moemail)
print(len(moemail))
#Todo: copy the extracted information to the clipboard
results = '\n'.join(justnumber)+'\n'+ '\n'.join(moemail)

print(results)
pyperclip.copy(results)

