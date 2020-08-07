import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
import os
def ca(dir):
    for path,subdirnames,filenames in os.walk(dir, topdown=False):
        print(path)
        print(subdirnames)
        print(filenames)
        for filename in filenames:
            print(filename)
            img_path=os.path.join(path,filename)
            image=cv2.imread(img_path)	    
            ca1(image,img_path)
def ca1(image,img_path):

    unknown_image = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(unknown_image) # detects all the faces in image
    t = len(face_locations)
    print(len(face_locations))
    print(face_locations)

    # Drawing rectangles over the faces
    pil_image = PIL.Image.fromarray(unknown_image)
    for face_location in face_locations:
    	#print(face_location)
    	top,right,bottom,left =face_location
    	draw_shape = PIL.ImageDraw.Draw(pil_image)
    	im = PIL.Image.open(img_path)
    	im = im.crop((left, top, right, bottom))
    	im.save(img_path+".jpg")    
    	draw_shape.rectangle([left, top, right, bottom],outline="blue")   	
ca('im/male/male')
'''
import PIL.Image
import PIL.ImageDraw
im = PIL.Image.open('mm.jpg').convert('L')
im1 = PIL.Image.open('mm.jpg')
left=384
top=190
right=474
bottom=245
im = im.crop((left, top, right, bottom))
im.save('22.jpg')
im1 = im1.crop((left, top, right, bottom))
im1.save('23.jpg')
	'''
