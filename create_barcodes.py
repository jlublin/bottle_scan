#!/usr/bin/env python3

# ./create_barcodes.py 96
# inkscape output.svg --export-pdf=output.pdf
# caja output.pdf
# Ctrl-P -> Page Handling -> Page Scaling: None
# Print

import sys
import os
import barcode
import xml.etree.ElementTree as ET

mminpx = 3.543307
width = 60
height = 30
offset_x = 5.0 * mminpx
offset_y = 3.5 * mminpx
delta_x = 70.0
delta_y = 37.0
delta_xpx = delta_x * mminpx
delta_ypx = delta_y * mminpx

if(__name__ == '__main__'):

	if(len(sys.argv) < 2):
		print('Usage: {} <start-id>'.format(sys.argv[0]))
		sys.exit()

	try:
		start_id = 2000000 + int(sys.argv[1]) # 2xxx xxxx is EAN-8 free range
	except ValueError:
		print('Not a valid id')
		sys.exit()

	stree = ET.parse('skeleton.svg')
	sroot = stree.getroot()
	group = sroot[0]

	for (i, id) in zip(range(3*8), range(start_id, start_id + 3*8)):
		barcode.generate('ean8', str(id), output='barcode')

		btree = ET.parse('barcode.svg')
		broot = btree.getroot()

		g = ET.SubElement(group, 'g')
		g.attrib['transform'] = 'matrix({},{},{},{},{},{})'.format(
								width/35,
								0,
								0,
								height/23,
								delta_xpx * (i // 8) + offset_x,
								delta_ypx * (i % 8) + offset_y)

		for c in broot[1:]:
			g.append(c)

	os.remove('barcode.svg')

	ET.register_namespace('','http://www.w3.org/2000/svg')
	stree.write('output.svg')

