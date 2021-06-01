#! python3
# search_pypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4

# Display text while downloading the search result page
print('Searching...')

res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
link_elements = soup.select('.package-snippet')
num_open = min(5, len(link_elements))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elements[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)