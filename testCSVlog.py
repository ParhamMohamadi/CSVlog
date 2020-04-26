import CSVlog
import time

MyTestData = CSVlog.DataCSVlogger('TestData')
MyTestData.WriteData(time.strftime("%d/%m/%Y-%H:%M"), 1, 20)