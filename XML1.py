from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('items.xml')

items = mydoc.getElementsByTagName('item')
#print(type(items))
# one specific item attribute
'''print('Item #2 attribute:')
print(items[1].attributes['name'].value)

# all item attributes
print('\nAll attributes:')
for elem in items:
    print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')
print(items[0].firstChild.data)
print(items[1].childNodes[0].data)'''

# all items data
i = 0
print('\nAll item data:')
for elem in items:
    print(str(elem.firstChild.data)+'   ' + str(items[i].attributes['name'].value))
    #print(items[i].attributes['name'].value)
    i += 1

'''
    <data>
    <items>
        <item name="item1">item1abc</item>
        <item name="item2">item2abc</item>
    </items>
</data>
'''