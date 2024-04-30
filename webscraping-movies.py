
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2024/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

# Find the table containing movie data
table = soup.find('table', class_='a-bordered')

# Create a new Excel workbook and select the active worksheet
workbook = xl.Workbook()
worksheet = workbook.active

# Add column headers
worksheet.append(['Rank', 'Movie', 'Release Date', 'Total Gross', 'Theaters', 'Average Gross per Theater'])

# Extract data from the top 5 rows in the table and add it to the Excel worksheet
rows = table.find_all('tr')[1:6]  # Select only the top 5 rows
for row in rows:
    cols = row.find_all('td')

    # Extract text from each column in the row
    rank = cols[0].get_text(strip=True)
    movie = cols[1].get_text(strip=True)
    release_date = cols[8].get_text(strip=True)
    total_gross_text = cols[7].get_text(strip=True)
    theaters_text = cols[6].get_text(strip=True)
    
    # Format Total Gross and Average Gross per Theater as currency
    if total_gross_text != '-':
        total_gross = float(total_gross_text.replace('$', '').replace(',', ''))
        total_gross_formatted = '${:,.2f}'.format(total_gross)
    else:
        total_gross_formatted = '-'

    if theaters_text != '-':
        theaters = float(theaters_text.replace(',', ''))
        average_per_theater = float(total_gross) / theaters if theaters != 0 else 0
        average_per_theater_formatted = '${:,.2f}'.format(average_per_theater)
    else:
        theaters = 0
        average_per_theater_formatted = '-'

    # Add data to the Excel worksheet
    worksheet.append([rank, movie, release_date, total_gross_formatted, theaters_text, average_per_theater_formatted])

# Apply bold font to the header row
for cell in worksheet[1]:
    cell.font = Font(bold=True)

# Save the Excel workbook with the desired name
workbook.save('BoxOfficeReport.xlsx')

#print("Data saved to 'BoxOfficeReport.xlsx'")

print(title.text)
##
##
##
##

