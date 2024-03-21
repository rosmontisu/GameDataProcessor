from PyQt5.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg

class LineChartWidget(QWidget):
    def __init__(self, data):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.plotWidget = pg.PlotWidget()
        self.layout.addWidget(self.plotWidget)

        self.plotData(data)

    def plotData(self, data):
        # data는 (x, y) 튜플의 리스트여야 합니다.
        x, y = zip(*data)
        self.plotWidget.plot(x, y, pen='r')

class BarChartWidget(QWidget):
    def __init__(self, data):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.plotWidget = pg.PlotWidget()
        self.layout.addWidget(self.plotWidget)

        self.plotData(data)

    def plotData(self, data):
        # data는 카테고리 이름과 값의 튜플의 리스트여야 합니다.
        categories, values = zip(*data)
        bg = pg.BarGraphItem(x=range(len(values)), height=values, width=0.6)
        self.plotWidget.addItem(bg)
        self.plotWidget.getAxis('bottom').setTicks([list(enumerate(categories))])

