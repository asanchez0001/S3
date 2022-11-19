import tkinter.ttk
from tkinter.ttk import *
from tkinter import PhotoImage

import os

"""
Remember you have the BBB video converted into these?
Convert them into VP8, VP9, h265 & AV1. You can use the script that allows you to transform, or create a new 
script. If not, you can do it manually.

Try to create a new video as the one of the 4 videos at the same time we saw in class, 
and please analyze by yourself and comment how these codecs work at each bitrate
"""

"""
https://mattgadient.com/x264-vs-x265-vs-vp8-vs-vp9-examples/
"""

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Video Codec Converter")

    window_width = 500
    window_height = 200
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # find the center point
    center_x = int(screen_width // 2 - window_width // 2)
    center_y = int(screen_height // 2 - window_height // 2)
    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    icon = PhotoImage(file='/Users/alvaro/Desktop/icon.png')
    window.iconphoto(False, icon)

    Label(window, text='Choose a video resolution').pack()
    size = Combobox(window, values=('720p', '480p', '360x240', '160x120'))
    size.pack(fill=tkinter.Y, padx=2, pady=2)

    Label(window, text='Choose a video codec').pack()
    codec = Combobox(window, values=('VP8', 'VP9', 'H265', 'AV1'))
    codec.pack(fill=tkinter.Y, padx=2, pady=2)


    def start_converter():
        path_to_file = 'BBB_CUT.mp4'
        codecs = {'vp8': 'webm', 'vp9': 'webm', 'libx265': 'mp4', 'libaom-av1': 'webm'}

        current_codec = codec.get().lower()
        if current_codec == 'h265':
            current_codec = 'libx265'
        if current_codec == 'av1':
            current_codec = 'libaom-av1'
        current_size = size.get()

        if current_size == '720p' or current_size == '480p':
            os.system(
                'ffmpeg -i {0} -vf scale=-1:{1} -c:v {3} BBB_CUT_{2}_{3}.{4}'.format(path_to_file, current_size[:3],
                                                                                     current_size, current_codec,
                                                                                     codecs[current_codec]))
        else:
            os.system('ffmpeg -i {0} -vf scale={1} -c:v {3} BBB_CUT_{2}_{3}.{4}'.format(path_to_file, current_size,
                                                                                        current_size, current_codec,
                                                                                        codecs[current_codec]))


    Button(window, text="Convert", command=start_converter).pack(side='bottom')

    window.mainloop()
