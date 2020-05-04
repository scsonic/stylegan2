import cv2
import numpy as np
import glob

img_array = []
fakes_array = []

# scan_dir = '../../fakes*.png'
scan_dir = "/home/scsonic/Desktop/stylegan2_result_only_copy/fakes/fakes*.png"

file_list = glob.glob(scan_dir)
file_list = sorted(file_list)


def get_sub_frame(src, x, y, len):
    # x = 0~31
    # y = 0~31
    # note: size = 128
    s = len * 128
    return src[x*128:x*128+s, y*128:y*128+s]


def openVideo(filename):
    fps = 10
    capSize = (128*8, 128*8)  # this is the size of my source video
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # cv2.CV_FOURCC('m', 'p', '4', 'v')  # note the lower case
    vout = cv2.VideoWriter()
    success = vout.open(filename, fourcc, fps, capSize, True)
    return vout


def runSplit():
    file = "../../fakes013236.png"
    img = cv2.imread(file)
    for w in range(0,32):
        for h in range(0,32):
            cc = get_sub_frame(img, w, h, 1)
            cv2.imwrite("video/split/x" + str(w) + "h" + str(h) + ".png", cc) ;


def getAcceptFromDir():
    dir = "video/split_v1/*.png"
    png_list = glob.glob(dir)
    png_list = sorted(png_list)
    print("png_list:", len(png_list))
    dic = {}
    accept_list = []
    for png in png_list:
        rep_str = png.replace("video/split_v1/", "")
        rep_str = rep_str.replace(".png", "")
        rep_str = rep_str.replace("x", " ")
        rep_str = rep_str.replace("h", " ")
        arr = [int(s) for s in rep_str.split() if s.isdigit()]
        x = arr[0]
        y = arr[1]
        accept_list.append((x, y))
        print(png, x, y)
    return accept_list


#  runSplit()
accept_list = getAcceptFromDir()
video_cell = 8
col_arr = []
p = 0
for x in range(video_cell):
    row_arr = []
    for y in range(video_cell):
        # row_arr.append((x%3, y%3))
        row_arr.append(accept_list[p])
        p = p + 1
    col_arr.append(row_arr)

out1 = openVideo("video/video_select1.mp4")

for filename in file_list:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    #fakes_array.append(filename)
    print("filename=", filename, size)

    col_img = []
    for x in range(video_cell):
        row_img = []
        for y in range(video_cell):
            xx, yy = col_arr[x][y]
            row_img.append(get_sub_frame(img, xx, yy, 1))
        col_img.append(cv2.hconcat(row_img))
    full = cv2.vconcat(col_img)
    cv2.imwrite("video/debug_full.png", full)
    out1.write(full)
out1.release()
# #
# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'MP4'), 15, size)
#
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
