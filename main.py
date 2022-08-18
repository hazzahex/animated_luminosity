import os
import csv
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.update()
frames_directory = filedialog.askdirectory()

# x_coord = int(input("What is the X coordinate to measure?... "))
# y_coord = int(input("What is the Y coordinate to measure?... "))

x_coord = 5
y_coord = 5

list_of_frames = []
ignored_frames = []
list_of_floats = []


def gather_frames():
    for root, directories, filenames in os.walk(frames_directory):
        for file in filenames:
            if ".png" in file:
                list_of_frames.append(os.path.join(root, file))
            else:
                ignored_frames.append(os.path.join(root, file))

    print(f'Found {len(list_of_frames)} frames')
    list_of_frames.sort()
    if len(ignored_frames) > 0:
        print(f'Ignored {len(ignored_frames)} files as they didn\'t have the .png extension')


def process_frames():
    for frame in list_of_frames:
        im = Image.open(frame)
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((x_coord, y_coord))
        list_of_floats.append(get_greyscale_float(r, g, b))


def get_greyscale_float(r, g, b):
    return ((r / 255) + (g / 255) + (b / 255)) / 3


def write_csv():
    with open('output.csv', 'w', newline='') as csv_out:
        csv_writer = csv.writer(csv_out, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['interval', 'float'])
        for index, item in enumerate(list_of_floats):
            csv_writer.writerow([index, item])


def run():
    gather_frames()
    process_frames()
    for f in list_of_floats:
        print(f)
    write_csv()


run()
