import os
import requests
from requests_file import FileAdapter

html_name = 'sample.html'
html_path = os.path.abspath(html_name)
drive, path = os.path.splitdrive(html_path)

s = requests.Session()
s.mount('file://', FileAdapter())
res = s.get('file://' + path.replace('\\', '/'))
print(res.text)
