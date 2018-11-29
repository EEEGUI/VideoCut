import cv2
import matplotlib.pyplot as plt


def video_cut(video_dir=None):
    cap = cv2.VideoCapture(video_dir)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    original_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    original_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    out1 = cv2.VideoWriter('video1.avi', fourcc, 15.0, (int(original_width), int(original_height/2)))
    out2 = cv2.VideoWriter('video2.avi', fourcc, 15.0, (int(original_width), int(original_height/2)))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret is True:
            frame1, frame2 = img_cut(frame)
            out1.write(frame1)
            out2.write(frame2)
            # cv2.imshow('frame1',frame1)
            # cv2.imshow('frame2', frame2)
            # cv2.waitKey(1)
            # if cv2.waitKey(1) & 0xFF == 27:
            #     break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out1.release()
    out2.release()
    cv2.destroyAllWindows()


def img_cut(img):
    """
    将图片分为上下两部分
    :param img:
    :return:
    """
    row = img.shape[0]

    img1 = img[0:int(row/2)]
    img2 = img[int(row/2):]

    return img1, img2


if __name__ == '__main__':
    test = 2
    if test ==1:
        # img_cut 测试
        img = cv2.imread(r'C:\Users\14622\Desktop\0.jpg')
        img1, img2 = img_cut(img)
        plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), 'gray')
        plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), 'gray')
        plt.show()
    else:
        # video_cut 测试
        video_cut(r'C:\0_document\video\VDO_0021.avi')