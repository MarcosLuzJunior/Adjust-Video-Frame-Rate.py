import getpass
import os
import glob
from pdf2image import convert_from_path

user = getpass.getuser() #For MAC users
input_dir_ = '/Folderpath/'
output_dir = '/Folderpath/'

if os.path.isdir(output_dir)== False: #Check if directory exists if not make one
    os.mkdir(output_dir)

pdfs_ = glob.glob(input_dir_ + '*.pdf') #Get all pdfs from input directory using glob.glob

for pdf in sorted(pdfs_):
    name = pdf.split('/')[-1].split('.')[0] #Split the pre and suffix
    print('Processing:' + name)

    try:
        pages = convert_from_path(pdf) #Use covert from path lib to covert pages of the pdfs into images
        for i, page in enumerate(pages):
            page.save(output_dir + name + '_page' + str(i) + '.png', 'PNG')#Save the new images using the page number and pdf name
    except Exception:
        continue

print('Finished')