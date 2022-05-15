# import image module
import os
from PIL import Image
from PIL import ImageFilter

open_dir = './archive'

save_dir = './archive_filtered'
if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

save_dir2 = './archive_filtered2'
if not os.path.isdir(save_dir2):
    os.mkdir(save_dir2)

list = os.listdir(open_dir)

for i in list:
    open_directory = open_dir + "/" + i
    save_directory = save_dir + "/" + i
    save_directory2 = save_dir2 + "/" + i
    filename = os.listdir(open_directory)

    for j in filename:
        open_image = open_directory + "/" + j
        imageObject = Image.open(open_image)

        edgeEnhanced = imageObject.filter(ImageFilter.EDGE_ENHANCE)
        moreEdgeEnhanced = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)

        if not os.path.isdir(save_directory):
            os.mkdir(save_directory)
        save_image = save_directory + "/" + j
        edgeEnhanced.save(save_image, format=None)

        if not os.path.isdir(save_directory2):
            os.mkdir(save_directory2)
        save_image2 = save_directory2 + "/" + j
        moreEdgeEnhanced.save(save_image2, format=None)

        print(open_image, "fin")