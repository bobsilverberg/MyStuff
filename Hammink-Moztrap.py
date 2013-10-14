from bs4 import BeautifulSoup
import requests

r = requests.get('http://mzl.la/GAeMs7', verify=False)
bs = BeautifulSoup(r.content)
headers = bs.select('header.itemhead')
results = []
for header in headers:
    result = {'name': header.select('h3.name')[0].contents[0]}
    for status in ('invalidated', 'blocked', 'failed', 'passed'):
        result[status] = header.select('a.%s' % status)[0].contents[0]
    results.append(result)

print results
