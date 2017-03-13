from lxml import etree


tree = etree.parse('query_result.xml')
root = tree.getroot()


names = root.xpath("//field[@name='name']/text()")
cities = root.xpath("//field[@name='city']/text()")
addresses = root.xpath("//field[@name='address']/text()")
ap_classes = root.xpath("//field[@name='class']/text()")
states = root.xpath("//field[@name='state']/text()")
developer_offers = root.xpath("//field[@name='developer_offer']/text()")

apartments = []
for child in root:
    name = child[1].text
    city = child[2].text
    address = child[3].text
    ap_class = child[4].text
    state = child[5].text
    developer_offer = child[6].text
    apartments.append([name, city, address, ap_class, state, developer_offer])
print(apartments)

print('Total/Unique names: ', len(names), '/', len(set(names)))
print('-' * 20)
print('Unique states: ', set(states))
print('-' * 20)
print('Unique developers_offers: ', set(developer_offers))
print('-' * 20)
print('Total cities: ', len(set(cities)))
print('Unique cities: ', set(cities))
print('-' * 20)
print('Total addresses: ', len(addresses))
print('-' * 20)
print('Unique classes: ', set(ap_classes))

import django
django.setup()

from .main.models import Apartment

for a in apartments:
    if a[0] is not None and a[2] is not None:
        q = Apartment(title=a[0], city=a[1], address=a[2], ap_class=a[3], state=a[4], developer_offer=a[5])
        q.save()
