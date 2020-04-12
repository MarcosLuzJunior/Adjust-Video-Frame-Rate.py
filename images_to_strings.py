import os
import pytesseract as py
import glob
import multiprocessing

# Define Class
class OCRCells():
    # Define function that takes 3 arguments including itself
    def process_image(self, path, out_dir):
        
        # Obtain the contours path (input directory + contours)
        contours_path = path + "/contours/"
        # Get all tbe .pgn files in the contours folder and index it to the img_path list
        img_path = glob.glob(contours_path + '*.png')
    
        for image in img_path:
            # In the FOR loop for each image in the list obtain name of the image with the image.split('/)[-1] notation
            # filename = os.path.splitext(image.split('/')[-1])
            filename = image.split('/')[-1].split('.')[0]
            # For each image in the list obtain the folder name
            contract_name = image.split('/')[7]
            image.split()
            print('Processing file name:' + filename)
            
            # If the directory has not yet been created, make a directory 
            if os.path.isdir(out_dir + contract_name) == False:
                os.mkdir(out_dir + contract_name)
                
            with open(os.path.join(out_dir, contract_name, filename) + '.txt', 'w+') as f:

                # Convert image to string
                text = py.image_to_string(image, config='--psm 6')
                f.write(text)
                

def main(in_dir, out_dir):
    
    ob = OCRCells()
    input_dir = sorted(glob.glob(in_dir + "*"))
    
    for item in input_dir:
        ob.process_image(item, out_dir)

        
if __name__ == '__main__':

    out_dir = '/folderpath/'
    in_dir = '/folderpath/'

    main(in_dir, out_dir)