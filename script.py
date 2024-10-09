import xml.etree.ElementTree as ET

def update_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for elem in root.iter('example'):
        elem.text = 'Updated Value'

    tree.write(file_path)

if __name__ == "__main__":
    update_xml('config.xml')
    print("XML file updated successfully.!!")
