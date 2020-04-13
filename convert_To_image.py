import getpass
import os
import glob
from pdf2image import convert_from_path

user = getpass.getuser()
input_dir_ = '/Users/' + user + '/Downloads/Forum_Pass/pdf/'
output_dir = '/Users/' + user + '/Downloads/Forum_Pass/tables/png_of_pdf/'

if os.path.isdir(output_dir)== False:
    os.mkdir(output_dir)

pdfs_ = glob.glob(input_dir_ + '*.pdf')

for pdf in sorted(pdfs_):
    name = pdf.split('/')[-1].split('.')[0]
    print('Processing:' + name)

    try:
        pages = convert_from_path(pdf)
        for i, page in enumerate(pages):
            page.save(output_dir + name + '_page' + str(i) + '.png', 'PNG')
    except Exception:
        continue

print('Finished')