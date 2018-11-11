import re
import requests
import time
site = "http://stankin.ru"

pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+)"')
#html=requests.get("http://stankin.ru").text
#links=pattern.findall(html)
all_links = []
full_links = []
def get_links(address, index):
  html=requests.get(address).text
  links=pattern.findall(html)
  next_links = []
  for link in links:
    if ".png" in link:
      continue
    elif ".css" in link:
      continue
    elif link.startswith("/"):
      full_links.append(site + link)
    elif not link.startswith('http') and not link.startswith('/'):
      full_links.append(site + '/' + link)
    else:
      full_links.append(link)
  if (index-1<0):
    return next_links
  for link in full_links:
    print (link)
    time.sleep(2)
    next_links = get_links(link, index - 1)
    all_links.extend(next_links)
  full_links.extend(all_links)
 # return full_links
#for link in get_links(site, 2):
  #print (link)
get_links(site, 2)
