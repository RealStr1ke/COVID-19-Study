import os
import csv

dataCDC = './cases.csv'
stateInitials = ["al","ak","az","ar","ca","co","ct","de","dc","fl","ga","hi","id","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","pa","pr","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy"]
def getData(folder, states):
  for state in states:
    file = state +"_cases.csv"
    filePath = os.path.join("/" + folder, file)
    if os.path.exists(filePath):
      os.remove(filePath)
    print(file)
    newFile = open(file, "w")
    newFilePath = "./" + folder + "/" + file
    os.rename("./" + file, newFilePath)
    with open (newFilePath, mode='w') as data:
      headers = ['date', 'new_cases']
      writer = csv.DictWriter(data, fieldnames=headers)

      writer.writeheader()
      with open (dataCDC, mode='r') as cases:
        reader = csv.reader(cases)
        for row in reader:
          if row[1].lower() == state:
            writer.writerow({'date': row[0], 'new_cases': row[2]})
      # writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
getData("data", stateInitials )