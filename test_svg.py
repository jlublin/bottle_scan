#!/usr/bin/env python3

import xml.etree.ElementTree as ET

stree = ET.parse('skeleton.svg')
btree = ET.parse('barcode.svg')

sroot = stree.getroot()
broot = btree.getroot()

g = sroot[0]

for child in g:
	for c in broot[1:]:
		child.append(c)

ET.register_namespace('','http://www.w3.org/2000/svg')
stree.write('output.svg')

