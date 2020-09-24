import PIL
from PIL import Image
from IPython.display import display

img = Image.open("/content/tech1.jpg")
h = int(img.height)
w = int(img.width)
print("INITIAL DIMENSIONS")
print(h)
print(w)
display(img)

choice = int(input("Enter 1 -SHRINK, 2- ZOOM ,3-QUIT"))
while choice!=3:
    if(choice == 1):
        factor = int(input("Enter factor to shrink "))
        h = int(h/factor)
        w = int(w/factor)
        print("UPDATED DIMENSIONS")
        print(h)
        print(w)
        img=img.resize((w,h))
    elif(choice == 2):
        factor = int(input("Enter factor to zoom "))
        h = int(h*factor)
        w = int(w*factor)
        print("UPDATED DIMENSIONS")
        print(h)
        print(w)
        img=img.resize((w,h))
    display(img)
    choice = int(input("\n\n\nEnter 1 -SHRINK, 2- ZOOM ,3-QUIT"))



