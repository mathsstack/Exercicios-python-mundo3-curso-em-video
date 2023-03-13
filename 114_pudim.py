import urllib
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br')
    
except urllib.request.URLError:
    print("The website isn't acessible")
    
else:
    print('The website it´s acessible')
