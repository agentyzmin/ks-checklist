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
