from PyQt5.Qt import *
import time


class SearchProductBatchDetailThread(QThread):
    """该类用于刷新产品批次查询界面"""
    update_date = pyqtSignal()  # 自定义一个信号

    def __init__(self):
        super().__init__()

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            print("线程1")
            self.update_date.emit()  # 发射信号
            time.sleep(3)  # 每隔三秒发射一次
