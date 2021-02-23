import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

# one specific item attribute
#print('Item #2 attribute:')
#print(root[0][1].attrib)

# all item attributes
#how to get Attributes with thier Values
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)
        print(subelem.tag)
        print(subelem.text)
        

# one specific item's data
#print('\nItem #2 data:')
#print(root[0][1].text)

# all items data
#print('\nAll item data:')
#for elem in root:
   # for subelem in elem:
      #  print(subelem.text)
#


'''
    <data>
    <items>
        <item name="item1">item1abc</item>
        <item name="item2">item2abc</item>
    </items>
</data>
'''