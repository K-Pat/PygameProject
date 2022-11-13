import csv
setting_name = 'meteor change'
new_value = [15]
arr=[]
# with open('settings.csv') as csvfile:
#     csvfilereader = csv.reader(csvfile)
#     for i in csvfilereader:
#         arr.append(i)

# for i in range(len(arr)):
#     if setting_name in arr[i]:
#         arr[i+1] = new_value
#        #print(arr[i+1])

# with open('settings.csv', 'w') as csvfile:
#     csvfilewriter = csv.writer(csvfile)
#     csvfilewriter.writerows(arr)
def find_setting(name):
    x=None
    with open('settings.csv') as csvfile:
        csvfilereader = csv.reader(csvfile)
        for i in csvfilereader:
            if name in i:
                x = next(csvfilereader)
    if not(x==None):
        for i in x:
            x=int(i)
        return x
    else:
        return None

print(find_setting(setting_name))
