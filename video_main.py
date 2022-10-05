import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QSettings, QThread
import os
import sys
import cv2
import threading
sys.path.append(r'C:\Users\29566\Desktop\pyqt_learn\ui')
sys.path.append(r'C:\Users\29566\Desktop\pyqt_learn')
from ui.window import Ui_mainWindow
import global_flag

flag = True
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.init_login_info()
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.slot_init()  # 初始化槽函数
        self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        self.cap3 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        self.open_flag1 = self.cap1.open(0)
        self.open_flag2 = self.cap2.open(1)
        self.open_flag3 = self.cap3.open(2)

    def slot_init(self):
        self.ui.OpenCamButton.clicked.connect(self.button_open_camera_clicked)
        self.ui.PathOpenButton.clicked.connect(self.define_savepath)
        self.ui.SignupButton.clicked.connect(self.save_login_info)
        self.ui.StartCollectButton.clicked.connect(self.Para_check)
        self.ui.EndCollectButton.clicked.connect(self.End_collect)
        self.timer_camera.timeout.connect(self.show_all)  # 若定时器结束，则调用show_camera()

    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        settings.setValue("Frame", self.ui.FrameEditLine.text())
        settings.setValue("SavePath", self.save_path)
        settings.setValue("Scene", self.ui.SceneChosenBox.currentText())
        settings.setValue("Size", self.ui.SizeSetChosenBox.currentText())
        settings.setValue("ID", self.ui.ID_EditLine.text())
        settings.setValue("Repetition", self.ui.Repet_EditLine.text())
        settings.setValue("Action", self.ui.ActionEditLine.text())
        settings.setValue("CollNote", self.ui.plainTextEdit.toPlainText())
        settings.setValue("DatasetNote", self.ui.Annotation.toPlainText())


    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        self.ui.FrameEditLine.setText(settings.value("Frame"))
        self.ui.ShowPathButton.setToolTip(settings.value("SavePath"))
        self.ui.SceneChosenBox.setCurrentText(settings.value("Scene"))
        self.ui.SizeSetChosenBox.setCurrentText(settings.value("Size"))
        self.ui.ID_EditLine.setText(settings.value("ID"))
        self.ui.Repet_EditLine.setText(settings.value("Repetition"))
        self.ui.ActionEditLine.setText(settings.value("Action"))
        self.ui.plainTextEdit.setPlainText(settings.value("CollNote"))
        self.ui.Annotation.setPlainText(settings.value("DatasetNote"))
        self.ui.ActionEditLine.setText(settings.value("Action"))
        self.save_path = settings.value("SavePath")


    def Para_check(self):
        global save_path
        self.FrameRate = self.ui.FrameEditLine.text()
        self.Scene = self.ui.SceneChosenBox.currentText()
        self.Size = self.ui.SizeSetChosenBox.currentText()
        self.ID = self.ui.ID_EditLine.text()
        self.Rep = self.ui.Repet_EditLine.text()
        self.Action = self.ui.ActionEditLine.text()
        safe_flag = True
        if len(self.FrameRate) == 0:
            self.error_dis('请输入采样帧数')
            safe_flag = False
        if self.Scene == '...':
            self.error_dis('请设置文件存储路径')
            safe_flag = False
        if self.ID == 0:
            self.error_dis('请输入人员编号')
            safe_flag = False
        elif len(self.ID) != 4 or self.ID[0] != 'P':
            self.error_dis('请填写正确人员编号')
            safe_flag = False
        if self.Rep == 0:
            self.error_dis('请输入重复次数')
            safe_flag = False
        elif len(self.Rep) != 4 or self.Rep[0] != 'R':
            self.error_dis('请填写正确重复次数')
            safe_flag = False
        if len(self.Action) == 0:
            self.error_dis('请输入动作类别')
            safe_flag = False
        elif len(self.Action) != 4 or self.Action[0] != 'A':
            self.error_dis('请填写正确动作信息')
            safe_flag = False
        if self.save_path != '...':
            self.Path = self.save_path
        if safe_flag:
            self.ui.StartCollectButton.setDisabled(0)
            self.ui.OpenCamButton.setDisabled(0)
            self.ui.FrameEditLine.setDisabled(0)
            self.ui.PathOpenButton.setDisabled(0)
            thr = threading.Thread(target=self.Collect_all)
            thr.start()
            # thr.join()


    def End_collect(self):
        global flag
        flag = False

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:
            if self.open_flag1 and self.open_flag2 and self.open_flag3 == False:  # flag表示open()成不成功
                self.error_dis('请检查三个相机连接情况')
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.ui.OpenCamButton.setText('关闭摄像头')
        else:
            self.timer_camera.stop()  # 关闭定时器
            # self.cap1.release()  # 释放视频流
            # self.cap2.release()  # 释放视频流
            # self.cap3.release()  # 释放视频流
            self.ui.View_1.clear()  # 清空视频显示区域
            self.ui.View_2.clear()  # 清空视频显示区域
            self.ui.View_3.clear()  # 清空视频显示区域
            self.ui.OpenCamButton.setText('打开摄像头')

    # def Collect_Cam(self, path, scene, person, action, fr):
    #     global flag
    #     if fr == 0:
    #         self.total_path_1 = '{root}/{s}C001{p}{a}'.format(root=path, s=scene, p=person, a=action)
    #         if not os.path.exists(self.total_path_1):
    #             os.mkdir(self.total_path_1)
    #     while self.cap1.isOpened() and flag == True:
    #         ret, frame = self.cap1.read()
    #         frame_index = f'F{fr:03d}.jpg'
    #         frame = cv2.resize(frame, (640, 480))  # 把读到的帧的大小重新设置为 640x480
    #         cv2.imwrite(os.path.join(self.total_path_1, frame_index), frame)

    def Collect_Cam1(self, fr):
        if fr == 0:
            path_1 = '{root}/{s}{e}C001{p}{r}{a}'.format(root=self.Path, s=self.Scene,
                                                                    e=self.Size, p=self.ID,
                                                                    r=self.Rep, a=self.Action)
            self.total_path_1 = path_1 + '.mp4'
            self.videoWriter1 = cv2.VideoWriter(self.total_path_1, self.fourcc, int(self.FrameRate), (640, 480))
        if self.cap1.isOpened():
            ret, frame = self.cap1.read()
            self.videoWriter1.write(frame)

    def Collect_Cam2(self, fr):
        if fr == 0:
            path_2 = '{root}/{s}{e}C002{p}{r}{a}'.format(root=self.Path, s=self.Scene,
                                                                    e=self.Size, p=self.ID,
                                                                    r=self.Rep, a=self.Action)
            self.total_path_2 = path_2 + '.mp4'
            self.videoWriter2 = cv2.VideoWriter(self.total_path_2, self.fourcc, int(self.FrameRate), (640, 480))
        if self.cap2.isOpened():
            ret, frame = self.cap2.read()
            self.videoWriter2.write(frame)

    def Collect_Cam3(self, fr):
        if fr == 0:
            path_3 = '{root}/{s}{e}C003{p}{r}{a}'.format(root=self.Path, s=self.Scene,
                                                                    e=self.Size, p=self.ID,
                                                                    r=self.Rep, a=self.Action)
            self.total_path_3 = path_3 + '.mp4'
            self.videoWriter3 = cv2.VideoWriter(self.total_path_3, self.fourcc, int(self.FrameRate), (640, 480))
        if self.cap3.isOpened():
            ret, frame = self.cap3.read()
            self.videoWriter3.write(frame)

    def Only_Show_Cam(self, cam):
        if cam == 0:
            flag, self.image = self.cap1.read()  # 从视频流中读取
        elif cam == 1:
            flag, self.image = self.cap2.read()  # 从视频流中读取
        else:
            flag, self.image = self.cap3.read()  # 从视频流中读取
        show = cv2.resize(self.image, (self.s_size[0], self.s_size[1]))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        if cam == 0:
            self.ui.View_1.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
        elif cam == 1:
            self.ui.View_2.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
        else:
            self.ui.View_3.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def show_all(self):
        Show_size = self.ui.ShownSizebox.currentText()
        if Show_size == '640*480':
            self.s_size = [640, 480]
        else:
            self.s_size = [400, 300]
        self.Only_Show_Cam(0)
        self.Only_Show_Cam(1)
        self.Only_Show_Cam(2)

    def Collect_all(self):
        global flag
        flag = True
        cnt = 0
        # begin_time = time.time()
        self.ui.ShowCollectStatus.setText('采集进行中')
        while flag:
            self.Collect_Cam1(cnt)
            self.Collect_Cam2(cnt)
            self.Collect_Cam3(cnt)
            cnt += 1
            p_t = round(cnt/int(self.FrameRate), 2)
            self.ui.ShowCollectTime.setText(str(p_t))
            # cur_time = f'{(time.time() - begin_time):.2f}秒'
            # self.ui.ShowCollectTime.setText(cur_time)
        self.videoWriter1.release()
        self.videoWriter2.release()
        self.videoWriter3.release()
        self.cnt = cnt
        self.ui.ShowCollectStatus.setText('正在检查文件完整性')
        self.Check_file()

    def Check_file(self):
        dirs = os.listdir(self.Path)
        dir_list = sorted(dirs, key=lambda x: os.path.getmtime(os.path.join(self.Path, x)), reverse=True)
        inter_flag = [0,0,0]
        t = 0
        d1, p1 = os.path.split(self.total_path_1)
        d2, p2 = os.path.split(self.total_path_2)
        d3, p3 = os.path.split(self.total_path_3)
        gen_list = [p1, p2, p3]
        for s, dir in enumerate(dir_list):
            if dir in gen_list:
                inter_flag[s] = 1
            else:
                inter_flag[s] = 0
            if s == 2:
                break
        for i in inter_flag:
            if i == 0:
                self.ui.ShowCollectStatus.setText('文件不完整')
            else:
                t += 1
        if t == 3:
            self.ui.ShowCollectStatus.setText('采集成功')


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

