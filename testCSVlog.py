import CSVlog
import time

MyTestData = CSVlog.DataCSVlogger('TestData')
MyTestData.WriteData(time.strftime("%d/%m/%Y-%H:%M"), 1, 200)
MyTestData.__del__()