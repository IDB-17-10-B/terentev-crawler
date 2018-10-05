import re
import requests
import time
site = 'http://stankin.ru'
pattern = re.compile(r'href="(?P<http_address>[a-zA-Z0-9:?&=\/.]+)"')


def foo(curr_link, depth=3):
    text = requests.get(curr_link).text
    links = pattern.findall(text)

    new_links =[]
    for link in links:
        if link.startswith('/'):
            new_links.append(site + link)
        elif not link.startswith('/') and not link.startswith('http'):
            new_links.append(curr_link + '/' + link)
        elif link.startswith('http://stankin.ru'):
            new_links.append(link)

    if depth - 1 <= 0:
        return new_links

    for i, link in enumerate(new_links):
        time.sleep(2)
        print('send', link, i, len(new_links))
        new_links.extend(foo(link, depth-1))

    return new_links

