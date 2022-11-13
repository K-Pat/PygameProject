import csv
class Setting:
    value=None
    name=''
    def __init__(self, name, value):
        self.value = value
        self.name = name
        arr=[]
        arr2=[]
        arr3=[]
        arr3.append(self.name)
        arr2.append(self.value)
        with open('settings.csv') as csvfile:
            csvfilereader = csv.reader(csvfile)
            for i in csvfilereader:
                arr.append(i)
        arr.append(arr3)
        arr.append(arr2)
        with open('settings.csv', 'w') as csvfile:
            csvfilewriter = csv.writer(csvfile)
            csvfilewriter.writerows(arr)
    def find_setting(self):
        x=None
        with open('settings.csv') as csvfile:
            csvfilereader = csv.reader(csvfile)
            for i in csvfilereader:
                if self.name in i:
                    x = next(csvfilereader)
        if not(x==None):
            return x
        else:
            return None
    def update_setting(setting_name, new_value):
        pass
