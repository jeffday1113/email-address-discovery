from emaildiscoverer import EmailDiscoverer
from bs4 import BeautifulSoup
import requests
from urlparse import urlparse

if __name__ == '__main__':
    disc = EmailDiscoverer('mit.edu')
    #print disc.subdomainBoolean('www.technology.mit.edu')
    disc.discover_emails()
    # r = requests.get('http://jana.com')
    # print r.content
    # soup = BeautifulSoup(r.content, 'html.parser')
    # for link in soup.find_all('a'):
    #     print link
