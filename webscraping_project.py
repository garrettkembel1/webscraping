from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


# Part 1
url= 'https://cryptoslate.com/coins/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

data = soup.find_all('tr')[1:6] 

for i in data:
    name = i.find('td', class_='col name').text.strip()
    
    price = i.find('td', class_='col price').text.strip()
    percent_change = i.find('td', class_='col change-24h').text.strip()
    
    
    price = float(price.replace('$', '').replace(',', ''))
    
    prev_price = round(price / (1 + float(percent_change.strip('%')) / 100), 2)

    print()
    print(f'Name: {name}')
    
    print(f'Price: {price:.2f}')
    print(f'Percent Change: {percent_change}')
    print(f'Previous Price: {prev_price:.2f}')
    


# Part 2
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from collections import Counter
import plotly.graph_objects as Plotly


url = 'https://quotes.toscrape.com/page/1/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

quotes = []

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

data = soup.find_all('div', class_='quote')

for i in data:
    text = i.find('span', class_='text').text.strip()
    author = i.find('small', class_='author').text.strip()
    tags = [tag.text.strip() for tag in i.find_all('a', class_='tag')]

    quotes.append({'text': text, 'author': author, 'tags': tags})


author_total = Counter([quote['author'] for quote in quotes])
most = max(author_total, key=author_total.get)
least = min(author_total, key=author_total.get)

print()
print("Author Statistics:")
print("Number of quotes by each author:")
for author, count in author_total.items():
    print(f"{author}: {count}")

print(f"Author with the most quotes: {most} ({author_total[most]} quotes)")
print(f"Author with the least quotes: {least} ({author_total[least]} quotes)")


length = [len(quote['text'].split()) for quote in quotes]
avg = sum(length) / len(length)
longest = max(quotes, key=lambda quote: len(quote['text']))
shortest = min(quotes, key=lambda quote: len(quote['text']))

print()
print("Quote Analysis:")
print(f"Average length of quotes: {avg:.2f} words")
print("Longest Quote:")
print(longest['text'])
print("Shortest Quote:")
print(shortest['text'])


tags = [tag for quote in quotes for tag in quote['tags']]
tag_distribution = Counter(tags)
most_popular = max(tag_distribution, key=tag_distribution.get)
total = len(tags)


print()
print('Tag Statistics:')
print(f"Most popular tag: {most_popular}")
print(f"Total tags used across all quotes: {total}")
print()

#Plotly
top = author_total.most_common(10)


names = []
counts = []
for author, count in top:
    names.append(author)
    counts.append(count)

figure = Plotly.Figure([Plotly.Bar(x=names, y=counts)])
figure.update_layout(title='Top 10 Authors and Their Number of Quotes', xaxis_title='Author', yaxis_title='Number of Quotes')
figure.show()


top = tag_distribution.most_common(10)


names = []
counts = []
for tag, count in top:
    names.append(tag)
    counts.append(count)

figure1 = Plotly.Figure([Plotly.Bar(x=names, y=counts)])
figure1.update_layout(title='Top 10 Tags Based on Popularity', xaxis_title='Tag', yaxis_title='Number of Quotes')
figure1.show()