import webbrowser as wb
import sys
import pyperclip
import requests
import re
import bs4
from selenium import webdriver



sys.argv
# wb.open('http://www.pythontutor.com/visualize.html#mode=edit')

if len(sys.argv)>1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('https://www.google.com/maps/'+address)


#wb.open('https://www.google.com/maps/'+address)

res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code   #200 means every is okay
ress=res.text
#print(ress)
print(len(res.text))
print(res.text[:500])

#badRes.get('https://automatetheboringstuff.com/files/kjsbfuigqeiufbkjbqkj')
#badRes.raise_for_status()  #for identifyin any 404 error

regex=re.compile(r'\w\w\w \d\d, \d\d\d\d', re.I)
mo=regex.findall(ress)
moo=''.join(mo)
#print(moo)
pyperclip.copy(moo)
am=pyperclip.paste()
wb.open('https://www.google.com/'+am)
print('https://www.google.com/'+am)

playfile=open('romeojuliet.rtf', 'wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)
    #print(chunk)
playfile.close()

#wb.open('https://www.amazon.com/gp/product/1593279922')

#---------------------------------------------

proxies = {
  "http": None,
  "https": None,
}
res= requests.get('https://www.amazon.com/gp/product/1593279922', proxies=proxies) #link
#res= requests.get('https://www.google.com/?client=safari', proxies=proxies)
print(res.raise_for_status)
soup=bs4.BeautifulSoup(res.text, 'html.parser')
elems=soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
#css path
elems[0].text.strip()


#------------------------------------

#from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')
elem=browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
elem.click()
elems=browser.find_elements_by_css_selector('p') #to find the paragraph elements
len(elems) #returns a list of matching paragragh elements in that page
searchElem=browser.find_element_by_css-selector('.search-field') #to select the search field
searchElem.send_keys('hari')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
browser.find_element_by_css-selector('html') #returns all the text in the webpage


