import os
import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/500/600')
result = response.read()
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__))) + '/cat.png'
with open(save_path, 'wb') as f:
    f.write(result)