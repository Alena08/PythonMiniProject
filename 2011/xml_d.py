import xml.etree.ElementTree as ET

#XML-Lesen
tree = ET.parse("person.xml")
root = tree.getroot()

for element in root:
    print(element.tag, element.attrib)
    print(element.attrib['gender'])
    for child in element:
        print(f"{child.tag}: {child.text}")
        if child.attrib:
            print(f"{child.attrib['color']}")
        for sChild in child:
            print(f"{sChild.tag}: {sChild.text}")

# XML-Schreiben

root = ET.Element("personen")

person1 = ET.SubElement(root, "person")
#person1.attrib = {"gender":"Female"}
person1.attrib['gender'] = "Female"
ET.SubElement(person1,"name").text = "Maria"
ET.SubElement(person1, "age").text = "25"

person2 = ET.SubElement(root, "person")
ET.SubElement(person2,"name").text = "Ali"
ET.SubElement(person2, "age").text = "55"

tree = ET.ElementTree(root)
tree.write("new.xml",encoding="utf-8",xml_declaration=True)
