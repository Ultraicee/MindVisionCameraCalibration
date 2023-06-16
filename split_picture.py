import cv2

if __name__ == "__main__":
    for i in range(49):  # 根据实际图片数量设置
        try:
            pic = cv2.imread("./Pictures/picture ({}).JPG".format(i + 1))  # 将Pictures文件夹中所有文件全选重命名为picture，会自动编号
            if not pic.shape[1] == 2560:
                print(i)
                continue
            pic_l = pic[:, :1280]
            pic_r = pic[:, 1280:]
            cv2.imwrite("L/mv_{}.JPG".format(i + 1), pic_l)
            cv2.imwrite("R/mv_{}.JPG".format(i + 1), pic_r)
            print("pic ({}) done".format(i + 1))
        except Exception as e:
            pass
