import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    #address = raw_input('Enter location: ')
    #url = 'http://python-data.dr-chuck.net/comments_42.xml'
    url = 'http://python-data.dr-chuck.net/comments_253587.xml'
    #if len(address) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

    results = tree.findall('.//count')

    number = 0
    for result in results:
        number += int(result.text)

    print number

    '''
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
    '''