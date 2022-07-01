from subprocess import Popen, PIPE
from lxml import etree
from io import StringIO
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
print("fetching: " + url)
get = Popen(['curl', '-s', '-A', user_agent, url], stdout=PIPE)
result = get.stdout.read().decode('utf8')
tree = etree.parse(StringIO(result), etree.HTMLParser())
str_tree = etree.tostring(tree, encoding='utf8', method='xml')
str_data = str_tree.decode()
print("writing file")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(str_data)