import re

links = []
pattern = r'(w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+)'
text = input()
while text:
    link = re.search(pattern, text)
    if link:
        links.append(link.group(1))

    text = input()

print('\n'.join(links))