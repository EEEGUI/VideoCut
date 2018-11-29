from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os, sys
from UiVideoCut import Ui_MainWindow
from VideoUtil import *
import time


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


def mat2qpixmap(img):
    """ numpy.ndarray to qpixmap
    """
    height, width = img.shape[:2]
    if img.ndim == 3:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif img.ndim == 2:
        rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        raise Exception("Unstatistified image data format!")
    qimage = QImage(rgb.data, width, height, 3*width, QImage.Format_RGB888)
    qpixmap = QPixmap.fromImage(qimage)
    return qpixmap


def show_qpixmap(label, img):
    """
    label 显示照片
    :param label:
    :param img:
    :return:
    """

    label_w = label.width()
    label_h = label.height()
    img = cv2.resize(img, (int(label_w), int(label_h)))
    qpixmap = mat2qpixmap(img)
    label.setPixmap(qpixmap)


class ProcessVideo(QThread):
    finished_signal = pyqtSignal(list)
    # mission_complete_signal = pyqtSignal()

    def __init__(self, video_dir, parent=None):
        super().__init__(parent)
        self.img_list = []
        self.video_dir = video_dir
        self.begin_time = 0.
        self.end_time = 1.
        self.duration = 0

    def run(self):
        self.begin_time = time.time()
        cap = cv2.VideoCapture(self.video_dir)
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        original_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        original_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        path = os.path.splitext(self.video_dir)[0]
        out1 = cv2.VideoWriter(path + '_part1.avi', fourcc, 30.0,
                               (int(original_width), int(original_height / 2)))
        out2 = cv2.VideoWriter(path + '_part2.avi', fourcc, 30.0,
                               (int(original_width), int(original_height / 2)))
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret is True:
                # 计时
                self.duration = time.time() - self.begin_time
                frame1, frame2 = img_cut(frame)
                out1.write(frame1)
                out2.write(frame2)
                self.img_list = []
                self.img_list.append(frame)
                self.img_list.append(frame1)
                self.img_list.append(frame2)
                self.img_list.append(self.duration)
                self.finished_signal.emit(self.img_list)
            else:
                self.img_list = []
                self.finished_signal.emit(self.img_list)
                break
        # Release everything if job is finished
        cap.release()
        out1.release()
        out2.release()


class VideoCut(QMainWindow, Ui_MainWindow):
    def __init__(self,  parent=None):
        super(VideoCut, self).__init__(parent)
        self.setupUi(self)
        self.video_dir = None


        # 信号/槽连接
        self.button_openfile.clicked.connect(self.get_file_dir)
        self.button_begin.clicked.connect(self.start_thread)
        self.button_cancel.clicked.connect(self.close)
        # self.button_begin.clicked.connect(self.test_function)

    def get_file_dir(self):
        file_dir = QFileDialog.getOpenFileName(caption='选择文件')
        self.video_dir = file_dir[0]

    def start_thread(self):
        if self.video_dir is None:
            QMessageBox.warning(self, '未选择文件', '请先选择文件')
        else:
            self.process_video = ProcessVideo(self.video_dir)
            self.process_video.finished_signal.connect(self.show_img)
            self.process_video.start()
            # self.process_video.mission_complete_signal(self.show_use_time)

    def show_img(self, img_list):
        if len(img_list) == 4:
            self.icd_time.display(int(img_list[3]))
            show_qpixmap(self.label_original, img_list[0])
            show_qpixmap(self.label_top, img_list[1])
            show_qpixmap(self.label_bottom, img_list[2])
        else:
            QMessageBox.information(self, '通知', '视频处理结束啦！吃饭啦！\n共计用时%d秒\n文件保存在原视频目录下'%(self.icd_time.value()))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = VideoCut()
    mainWindow.show()
    sys.exit(app.exec_())