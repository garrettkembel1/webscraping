
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2024/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title


table = soup.find('table', class_='a-bordered')


workbook = xl.Workbook()
worksheet = workbook.active


worksheet.append(['Rank', 'Movie', 'Release Date', 'Total Gross', 'Theaters', 'Average Gross per Theater'])

rows = table.find_all('tr')[1:6]  #
for i in rows:
    columns = i.find_all('td')

    
    rank = columns[0].get_text(strip=True)
    movie = columns[1].get_text(strip=True)
    release_date = columns[8].get_text(strip=True)
    gross_text = columns[7].get_text(strip=True)
    theaters_text = columns[6].get_text(strip=True)
    
  
    if gross_text != 0:
        total_gross = float(gross_text.replace('$', '').replace(',', ''))
        gross_format = '${:,.2f}'.format(total_gross)
    else:
        gross_format = 0

    if theaters_text != 0:
        theaters = float(theaters_text.replace(',', ''))
        average = float(total_gross) / theaters if theaters != 0 else 0
        average_format = '${:,.2f}'.format(average)
    else:
        theaters = 0
        average_format = 0

  
    worksheet.append([rank, movie, release_date, gross_format, theaters_text, average_format])


for cell in worksheet[1]:
    cell.font = Font(bold=True)


workbook.save('BoxOfficeReport.xlsx')


print(title.text)
##
##
##
##

