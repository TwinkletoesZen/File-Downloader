import requests

url = "https://query1.finance.yahoo.com/v7/finance/download/FM.TO?period1=1607647159&period2=1639183159&interval=1d&events=history&includeAdjustedClose=true"

r = requests.get(url, allow_redirects=True)
open('Data_2.csv', 'wb').write(r.content)
