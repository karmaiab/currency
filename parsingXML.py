import xml.etree.ElementTree as ET
tree = ET.parse('currency.xml')
root = tree.getroot()

root.tag
root.attrib

for child in root.findall('./currencys/currency'):
    name = child.get('name')
    year = child.get('year')
    for country in root.find('./currencys/currency/country'):
        title = country.get('title')

    print("Name: %s, Year: %s, Country: %s" %(name, year, title))