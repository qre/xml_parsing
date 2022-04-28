import xml.etree.ElementTree as ET

f = 'export_full.xml'
mytree = ET.parse(f)
myroot = mytree.getroot()

if __name__=='__main__':
        for node in mytree.findall('.//items/item'):
            x = node.attrib['name']
            print(x)
        num_items = len(myroot.findall(".//items/item"))
        print(num_items)
        for node2 in mytree.findall('.//items/item/parts/part'):
            if node2.attrib['name'] == 'Náhradní díly':
                for node3 in mytree.findall('.//items/item/parts/part/item'):
                    ndil = node3.attrib['name']
                    print('Náhradní díl:', ndil)
        num_dil = len(mytree.findall('.//items/item/parts/part/item'))
