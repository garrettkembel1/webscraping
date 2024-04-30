import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request







random_chapter = random.randrange(1,22)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)

else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
page = urlopen(webpage)
soup = BeautifulSoup(page, 'html.parser')
 
title = soup.title

print(soup.title.text)

page_verses = soup.findAll ('div', class_= 'p')

my_verses = []

for section_verses in page_verses:
    #soup.find('span', class_='verse')
    verse_list = section_verses.text.split('.')
    #print(verse_list)

    for v in verse_list:
        my_verses.append(v)

my_verses = [i for i in my_verses if i != ' ']

#print (my_verses)

my_choice = random.choice(my_verses)

print(f'Chapter: {random_chapter} Verse: {my_choice}')
    
