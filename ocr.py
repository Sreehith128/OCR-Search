from pytesseract import image_to_string
import cv2
import os
import re

def img2string(img_name):
	#to use OCR to convert image file to string
	img=cv2.imread(img_name)
	try:
		img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	except:
		print('Some error')
	return image_to_string(img).replace('\n','')
def fileSearch(dir_name,input_text):
	for img_name in os.listdir(dir_name):
		img_path=os.path.join(dir_name, img_name)
		if re.search('\\.png$|\\.jpeg$|\\.jpg$',img_name) and not os.path.isdir(img_path):

			img_content=img2string(img_path)
			res=img_content.find(input_text)
			if  res != -1:
				img=cv2.imread(img_path)
				cv2.imshow('Text related image',img)
				cv2.waitKey(0)
				
if __name__=='__main__':
	print('Enter path of directory to be searched:',end=' ')
	dir_path=input()
	print('Enter input string to be searched for: ',end=' ')
	input_text=input()
	fileSearch(dir_path,input_text)




