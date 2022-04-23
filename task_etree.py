import xml.etree.ElementTree as ET
with open("export.xml", mode='r', encoding='utf-8', errors='ignore') as f:
    file = f.read()
    mytree = ET.parse(f)
    myroot = mytree.getroot()
    print(myroot[0].tag)
    for x in myroot[0]:
        print(x.tag, x.attrib)
