#!/usr/bin/env python3

import sys
import barcode
import xml.etree.ElementTree as ET

if(__name__ == '__main__'):

	if(len(sys.argv) < 2):
		print('Usage: {} <start-id>'.format(sys.argv[0]))
		sys.exit()

	try:
		start_id = 1000000 + int(sys.argv[1])
	except ValueError:
		print('Not a valid id')
		sys.exit()

	stree = ET.parse('skeleton.svg')
	sroot = stree.getroot()
	group = sroot[0]

	for (i, id) in zip(range(3*7), range(start_id, start_id + 3*7)):
		barcode.generate('ean8', str(id), output='barcode')

		btree = ET.parse('barcode.svg')
		broot = btree.getroot()

		for c in broot[1:]:
			group[i].append(c)

	ET.register_namespace('','http://www.w3.org/2000/svg')
	stree.write('output.svg')

