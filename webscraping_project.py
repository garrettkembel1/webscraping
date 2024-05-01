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
    name = i.find('td',class_='col name').text.strip()
    
    price = i.find('td',class_='col price').text.strip()
    percent_change = i.find('td',class_='col change-24h').text.strip()
    
    
    price = float(price.replace('$','').replace(',',''))
    
    prev_price = round(price / (1+float(percent_change.strip('%'))/100),2)

    print()
    print(f'Name: {name}')
    
    print(f'Price: {price:.2f}')
    print(f'Percent Change: {percent_change}')
    print(f'Previous Price: {prev_price:.2f}')
    


# Part 2
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from collections import Counter



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

quotes = []

for page in range(1, 11):
    url = f'https://quotes.toscrape.com/page/{page}/'
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    data = soup.find_all('div',class_='quote')

    for i in data:
        text = i.find('span',class_='text').text.strip()
        author = i.find('small',class_='author').text.strip()
        tags = [tag.text.strip() for tag in i.find_all('a',class_='tag')]

        quotes.append({'text': text, 'author': author, 'tags': tags})


author_quotes = Counter([quote['author'] for quote in quotes])
most = max(author_quotes, key=author_quotes.get)
least = min(author_quotes, key=author_quotes.get)

print()
print('Author Stats:')
print('Quotes per Author:')
for author, count in author_quotes.items():
    print(f'{author}: {count}')

print(f'Author with the most quotes: {most} with {author_quotes[most]} quotes')
print(f'Author with the least quotes: {least} with {author_quotes[least]} quote(s)')

length = [len(quote['text'].split()) for quote in quotes]
avg = sum(length)/len(length)
longest = 0
shortest = 0

for i in quotes:
    text = i['text']
    if longest == 0 or len(text) > len(longest['text']):
        longest = i
    if shortest == 0 or len(text) < len(shortest['text']):
        shortest = i

print()
print('Quote Statistics:')
print(f'Average length: {avg:.2f} words')
print()
print('Longest Quote:')
print()
print(longest['text'])
print()
print('Shortest Quote:')
print()
print(shortest['text'])


tags = [tag for quote in quotes for tag in quote['tags']]
tag_distribution = Counter(tags)
most_popular = max(tag_distribution,key=tag_distribution.get)
total = len(tags)


print()
print('Tag Numbers:')
print(f'Most popular tag: {most_popular}')
print(f'Total tags used: {total}')
print()

# Plotly
from plotly.graph_objs import Layout
from plotly import offline


names = list(author_quotes.keys())
counts = list(author_quotes.values())


data = [{
    'type': 'bar',
    'x': names,
    'y': counts,
}]


layout = Layout(
    title='Quotes per Author',
    xaxis=dict(title='Author'),
    yaxis=dict(title='Quotes')
)


figure = {'data': data, 'layout': layout}


offline.plot(figure, filename='quotes.html')



tags = list(tag_distribution.keys())
counts = list(tag_distribution.values())

data = [{
    'type': 'bar',
    'x': tags,
    'y': counts,
}]


layout = Layout(
    title='Tag Rankings',
    xaxis=dict(title='Tag'),
    yaxis=dict(title='Quotes')
)


figure = {'data': data, 'layout': layout}


offline.plot(figure, filename='tag.html')