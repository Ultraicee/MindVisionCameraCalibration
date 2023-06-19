import os
import cv2
import re
from os.path import join


def natural_sort_key(s):
    """
    按文件名的结构排序，即依次比较文件名的非数字和数字部分
    """
    # 将字符串按照数字和非数字部分分割，返回分割后的子串列表
    sub_strings = re.split(r'(\d+)', s)
    # 如果当前子串由数字组成，则将它转换为整数；否则返回原始子串
    sub_strings = [int(c) if c.isdigit() else c for c in sub_strings]
    # 根据分割后的子串列表以及上述函数的返回值，创建一个新的列表
    # 按照数字部分从小到大排序，然后按照非数字部分的字典序排序
    return sub_strings


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def is_exist_dir(file_path):
    dirs_l = join(file_path, "L")
    if not os.path.exists(join(dirs_l)):
        os.makedirs(dirs_l)
    dirs_r = join(file_path, "R")
    if not os.path.exists(join(dirs_r)):
        os.makedirs(dirs_r)


def proc_img(file_dir='../Src/Pictures', save_path='../Output'):
    # 创建目录
    is_exist_dir(save_path)
    image_filenames = [x for x in os.listdir(file_dir) if is_image_file(x)]
    # 按文件名从小到大排序
    image_filenames.sort(key=natural_sort_key)  # filter‘.JPG’ and sort
    try:
        for i, image_filename in enumerate(image_filenames):
            pic = cv2.imread(join(file_dir, image_filename))
            H, W, C = pic.shape
            pic_l = pic[:, :W // 2]
            pic_r = pic[:, W // 2:]
            cv2.imwrite(join(save_path, "L/", image_filename), pic_l)
            cv2.imwrite(join(save_path, "R/", image_filename), pic_r)
            print("[{}/{}]".format(i + 1, len(image_filenames)),
                  image_filename, "done")
    except ValueError as e:
        print(e)
    print("Split Successfully.")


if __name__ == "__main__":
    proc_img()
    print("Done.")
