import cv2
import glob
from Tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


def vid_rate_adj(input, out_dir, fps, targetFormat):

    # Specify where you would like to save the gif and how it should be called
    save_to = out_dir + input.split('/')[-1].split('.')[0]

    i = 0
    # Use OpenCV to read the video
    video_input = cv2.VideoCapture(input)

    print('Saving Video Frames')
    while (video_input.isOpened()):
        ret, frame = video_input.read()
        try:
            if ret == True:
                cv2.imwrite(save_to + '-' + str(i) + targetFormat, frame)
                i += 1
        except:
            print("An exception occurred")

    video_input.release()
    cv2.destroyAllWindows()

    print('Preparing to adjust video rate')
    # Create an array to hold all the images frames recorded by on the video
    frames_rec = []

    # Now that the frames have been recorded we can read back into a variable
    frames = glob.glob(save_to + "*")
    for frame in sorted(frames):
        img = cv2.imread(frame)
        height, width, layers = img.shape
        size = (width, height)
        frames_rec.append(img)

    out = cv2.VideoWriter(save_to + '.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)
    cv2.VideoWriter()

    print('Saving new video rate version')
    for item in frames_rec:
        # writing to a image array
        out.write(frames_rec[item])
    out.release()

    print('Video rate has been adjusted')

def main():
    # Choose Frame Rate
    try:
        fpsr = int(input("Enter a desired frame rate: "))
    except:
        print('The value entered is not an integer please try again')

    # Choose the video location
    print("Please select the video: ")
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    Videochosen = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    # Choose where to save the modified video
    print("Please select a location to save the modified video: ")
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    save_location = filedialog.askdirectory()  # show an "Open" dialog box and return the path to the selected file

    vid_rate_adj(Videochosen, save_location, fpsr,'.jpeg')

if __name__ == '__main__':
    main()
