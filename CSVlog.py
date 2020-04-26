import csv


class DataCSVlogger:
    def __init__(self, filename):
        self.filename = filename
        self.DataLog = open(self.filename + '.csv', mode='w')
        self.Date_Writer = csv.writer(self.DataLog, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self.Date_Writer.writerow(['Time', 'Depth', 'Pressure'])

    def __del__(self):
        self.DataLog.close()

    def WriteData(self, time, meter=None, pressure=None):
        self.Date_Writer.writerow([time, meter, pressure])