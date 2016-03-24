import json
import urllib

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''


#url = 'http://python-data.dr-chuck.net/comments_42.json'
url = 'http://python-data.dr-chuck.net/comments_253591.json'

data = urllib.urlopen(url).read()

info = json.loads(data)
print 'User count:', len(info)

result = 0
for item in info['comments']:
    result += int(item['count'])

print result
'''
for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']
'''
