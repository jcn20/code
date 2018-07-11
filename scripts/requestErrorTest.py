import requests

res = requests.get('http://inventwithpython.com/page_that')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))