import xml.etree.ElementTree as ET

tree = ET.parse("dane.xml")
root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag, child.attrib)

for desc in root.iter('description'):
    print(desc.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie"):
    year = movie.find('year')
    if year.text == "1992":
        year.text = str(2023)
        year.set("year_changed", "yes")
        tree.write("year_changed.xml")
    else:
        pass

#
for movie in root.findall("./genre/decade/movie/[@multiple='yes']..."):
    print(movie.attrib)

