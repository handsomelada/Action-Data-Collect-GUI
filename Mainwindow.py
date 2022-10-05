from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QSettings
import time
import sys
import cv2
import split_frame
import threading
sys.path.append(r'C:\Users\29566\Desktop\pyqt_learn\ui')
sys.path.append(r'C:\Users\29566\Desktop\pyqt_learn')
from ui.window import Ui_mainWindow
import global_flag


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.init_login_info()
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.cap_0 = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 视频流
        # self.cap_1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # 视频流
        self.cap_2 = cv2.VideoCapture(1)  # 视频流
        self.cam = 0
        self.slot_init()  # 初始化槽函数

    def slot_init(self):
        self.ui.OpenCamButton.clicked.connect(self.button_open_camera_clicked)  # 若该按键被点击，则调用button_open_camera_clicked()
        self.ui.PathOpenButton.clicked.connect(self.define_savepath)
        self.ui.SignupButton.clicked.connect(self.save_login_info)
        self.ui.StartCollectButton.clicked.connect(self.Para_check)
        self.timer_camera.timeout.connect(self.show_all)  # 若定时器结束，则调用show_camera()

    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        settings.setValue("Frame", self.ui.FrameEditLine.text())
        settings.setValue("SavePath", self.save_path)
        settings.setValue("Scene", self.ui.SceneChosenBox.currentText())
        settings.setValue("ID", self.ui.ID_EditLine.text())
        settings.setValue("Action", self.ui.ActionEditLine.text())

    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        self.ui.FrameEditLine.setText(settings.value("Frame"))
        self.ui.ShowPathButton.setToolTip(settings.value("SavePath"))
        self.ui.SceneChosenBox.setCurrentText(settings.value("Scene"))
        self.ui.ID_EditLine.setText(settings.value("ID"))
        self.ui.ActionEditLine.setText(settings.value("Action"))
        self.save_path = settings.value("SavePath")

    def Para_check(self):
        FrameRate = self.ui.FrameEditLine.text()
        Scene = self.ui.SceneChosenBox.currentText()
        ID = self.ui.ID_EditLine.text()
        Action = self.ui.ActionEditLine.text()
        Path = self.save_path
        safe_flag = True
        if len(FrameRate) == 0:
            self.error_dis('请输入采样帧数')
            safe_flag = False
        if Path == '...':
            self.error_dis('请设置文件存储路径')
            safe_flag = False
        if len(ID) == 0:
            self.error_dis('请输入ID信息')
            safe_flag = False
        elif len(ID) != 4 or ID[0] != 'P':
            self.error_dis('请填写正确ID信息')
            safe_flag = False
        if len(Action) == 0:
            self.error_dis('请输入动作类别')
            safe_flag = False
        elif len(Action) != 4 or Action[0] != 'A':
            self.error_dis('请填写正确动作信息')
            safe_flag = False
        if Path != '...':
            Path = self.save_path
        if safe_flag:
            self.ui.StartCollectButton.setText('结束采集（动作结束）')
            thread_CAM_1 = threading.Thread(target=split_frame.start_collect_view_1, args=(Path, Scene, ID, Action))
            thread_CAM_2 = threading.Thread(target=split_frame.start_collect_view_2, args=(Path, Scene, ID, Action))
            thread_CAM_3 = threading.Thread(target=split_frame.start_collect_view_3, args=(Path, Scene, ID, Action))
            thread_CAM_1.start()
            thread_CAM_2.start()
            thread_CAM_3.start()
            self.ui.StartCollectButton.clicked.connect(self.get_collect_flag)

    def get_collect_flag(self):
        if self.ui.StartCollectButton.text() == '结束采集（动作结束）':
            global_flag.set_value('collect_flag',0)
            self.ui.StartCollectButton.setText('开始采集（动作开始）')
        else:
            global_flag.set_value('collect_flag',1)
            self.ui.StartCollectButton.setText('结束采集（动作结束）')

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            # flag = self.cap.open(self.cam)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            # if flag == False:  # flag表示open()成不成功
            #     msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=self.ui.OpenCamButton.Ok)
            # else:
            self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
            self.ui.OpenCamButton.setText('关闭摄像头')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap_0.release()  # 释放视频流
            self.cap_1.release()  # 释放视频流
            self.cap_2.release()  # 释放视频流
            self.ui.View_1.clear()  # 清空视频显示区域
            self.ui.View_2.clear()  # 清空视频显示区域
            self.ui.view_3.clear()  # 清空视频显示区域
            self.ui.OpenCamButton.setText('打开摄像头')

    def show_camera_1(self):
        flag, self.image = self.cap_0.read()  # 从视频流中读取

        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.ui.View_1.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def show_camera_2(self):
        flag, self.image = self.cap_1.read()  # 从视频流中读取

        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.ui.View_2.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def show_camera_3(self):
        flag, self.image = self.cap_2.read()  # 从视频流中读取

        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.ui.view_3.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def show_all(self):
        flag1, self.image1 = self.cap_0.read()  # 从视频流中读取
        # flag2, self.image2 = self.cap_1.read()  # 从视频流中读取
        flag3, self.image3 = self.cap_2.read()  # 从视频流中读取

        show1 = cv2.resize(self.image1, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        # show2 = cv2.resize(self.image2, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show3 = cv2.resize(self.image3, (640, 480))  # 把读到的帧的大小重新设置为 640x480

        show1 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        # show2 = cv2.cvtColor(show2, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        show3 = cv2.cvtColor(show3, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色

        showImage1 = QtGui.QImage(show1.data, show1.shape[1], show1.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        # showImage2 = QtGui.QImage(show2.data, show2.shape[1], show2.shape[0],
        #                          QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        showImage3 = QtGui.QImage(show3.data, show3.shape[1], show3.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.ui.View_1.setPixmap(QtGui.QPixmap.fromImage(showImage1))  # 往显示视频的Label里 显示QImage
        # self.ui.View_2.setPixmap(QtGui.QPixmap.fromImage(showImage2))  # 往显示视频的Label里 显示QImage
        self.ui.view_3.setPixmap(QtGui.QPixmap.fromImage(showImage3))  # 往显示视频的Label里 显示QImage
        # begin_time = time.time()
        # self.show_camera_1()
        # self.show_camera_2()
        # self.show_camera_3()
        # cv2.waitKey(1)
        # end_time = time.time()
        # print("捕获视频运行时间为",end_time-begin_time)
        # self.getID()

    def getFrameRate(self):
        FrameRate = self.ui.FrameEditLine.text()
        return FrameRate

    def getScene(self):
        Scene = self.ui.SceneChosenBox.currentText()
        return Scene

    def getID(self):
        ID = self.ui.ID_EditLine.text()
        if len(ID) == 0:
            self.error_dis('请输入ID信息')
        if len(ID) != 4:
            self.error_dis('请补充完整ID信息')
        print(ID)
        return ID

    def getAction(self):
        Action = self.ui.ActionEditLine.text()
        return Action

    def define_savepath(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        self.ui.ShowPathButton.setToolTip(directory1)
        self.save_path = directory1
        return directory1

    def error_dis(self, msg):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

if __name__ == '__main__':
    global_flag._init()
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = Window()  # 实例化Ui_MainWindow
    ui.show()  # 调用ui的show()以显示
    sys.exit(app.exec_())  # 不加这句，程序界面会一闪而过