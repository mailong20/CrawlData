import glob
from pascal_voc_writer import Writer
import xml.etree.ElementTree as ET
import os 

def change_xml():
# parse xml file
	src=r"E:\Dataset_Fashion\Fashion\train\labels"
	obj_list=glob.glob(src+"/**/*.xml",recursive=True)
	for path_sub in obj_list:
		tree = ET.parse(path_sub) 
		root = tree.getroot() # get root objet
		object = root.findall('object')
		for ob in object:
			name = ob.find('name').text
			print(name)
		# path = root.find('path').text
		# if filename.split('.')[0] =='xml' or filename.split('.')[1] =='xml':
		# 	root.find('filename').text = os.path.basename(path_sub).split('.')[0]+'.jpg'
		# 	root.find('path').text = os.path.basename(path_sub).split('.')[0]+'.jpg'
		# 	print(os.path.basename(path_sub).split('.')[0]+'.jpg')
		# tree.write(path_sub)
change_xml()