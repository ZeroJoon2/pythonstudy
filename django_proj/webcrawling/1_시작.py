import requests

from PIL import Image
from io import BytesIO

print('hello~')

url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
r.status_code
print(r.json())

url = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
google_logo = requests.get(url)

Image.open(BytesIO(google_logo.content))
