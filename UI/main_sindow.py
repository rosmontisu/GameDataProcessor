import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from widgets import LineChartWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameData Extractor")
        self.setGeometry(100, 100, 800, 600)  # 위치와 크기 설정
        self.initUI()

    def initUI(self):
        # 메인 위젯과 레이아웃 설정
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        # 추가적인 UI 컴포넌트 초기화...
        # 예시 데이터
        sampleData = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
        self.lineChartWidget = LineChartWidget(sampleData)
        self.mainLayout.addWidget(self.lineChartWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
