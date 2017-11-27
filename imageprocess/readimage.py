# from PIL import Image
# import matplotlib.pyplot as plt # plt 用于显示图片
# import matplotlib.image as mpimg # mpimg 用于读取图片
# import numpy as np
#
# im = Image.open('E:/1.png')
# a = np.array(im)
# print(a.shape)
# a1 = a[0:110, 0:110, :]
# a2 = a[0:110, 110:, :]
# print(a2.shape)
# a3 = a[110:, 0:110, :]
# a4 = a[110:, 110:, :]
# plt.imshow(a4)
# # plt.show()
#
# plt.savefig('E:/a4.png')
# # a2.save('E:/a2.png')
# # a3.save('E:/a3.png')
# # a4.save('E:/a4.png')



import os
def _load_image_set_index():
    """
    Load the indexes listed in this dataset's image set file.
    """
    # Example path to image set file:
    # self._devkit_path + /VOCdevkit2007/VOC2007/ImageSets/Main/val.txt
    # image_set_file = os.path.join(self._data_path, 'ImageSets', 'Main',
    #                               self._image_set + '.txt')
    image_set_file = 'E:/valdata1/val1.txt'
    out_file = r'E:\tf-faster-rcnn\data\ImageSets\Main\test.txt'
    assert os.path.exists(image_set_file), \
        'Path does not exist: {}'.format(image_set_file)
    with open(image_set_file) as f:
        image_index = [x.strip() for x in f.readlines()]
    out1= open(out_file,'w')
    for i in image_index:
        out1.write(i+'\n')
    out1.close()



def _load_train_data():
    train_dir = 'E:/traindata1/images/'
    out_train = r'E:\tf-faster-rcnn\data\ImageSets\Main\train.txt'
    out_trainval = r'E:\tf-faster-rcnn\data\ImageSets\Main\trainval.txt'
    out_val = r'E:\tf-faster-rcnn\data\ImageSets\Main\val.txt'
    file_list = os.listdir(train_dir)
    f1 = open(out_trainval, 'w')
    f2 = open(out_train, 'w')
    f3 = open(out_val, 'w')
    for file_obj in file_list:
        file_name, file_extend = os.path.splitext(file_obj)
        file_num = int(file_name)
        f1.write(file_name+'\n')
        if file_num % 10 != 0:
            f2.write(file_name+'\n')
        else:
            f3.write(file_name+'\n')

    f1.close()
    f2.close()
    f3.close()



def changesuffix():
    path =r'E:\tf-faster-rcnn\data\JPEGImages'
    files = os.listdir(path)
    for filename in files:
        portion = os.path.splitext(filename)
        # 如果后缀是.txt
        if portion[1] == ".png":
            # 重新组合文件名和后缀名
            newname = portion[0] + ".jpg"
            os.chdir(path)
            os.rename(filename, newname)








if __name__ == '__main__':
    changesuffix()



