from zipfile import *

'''with ZipFile('images1.zip','w',ZIP_DEFLATED) as f: #images.zip folder will be created with compresses images
    f.write('cb1.png')
    f.write('cb2.png')'''


'''f=ZipFile('images1.zip','r')
f.extractall()
f.close()'''

#print(dir(ZipFile))
#--alternatively---

'''import zipfile as zf

with zf.ZipFile('images2.zip','w',ZIP_DEFLATED) as z:
    print(z.write('sasuke.jpg'))

f=ZipFile('images2.zip','r') #what is need of assiging to f here
f.extractall()  #same here
f.close()'''

'''with zf.ZipFile('images2.zip','r') as z:
    z.extractall()'''
