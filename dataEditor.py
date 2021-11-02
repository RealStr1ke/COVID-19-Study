import os
import csv
import wget


dataCDC = './src/cases.csv'
stateInitials = ["al","ak","az","ar","ca","co","ct","de","dc","fl","ga","hi","id","il","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","ok", "or", "pa","pr","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy"]
def getData(folder, states):
  if os.path.exists(dataCDC):
    os.remove(dataCDC)
  print('Retrieving CDC data...')
  url = 'https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD'
  wget.download(url, './src/cases.csv')
  print('Retrieved CDC data.')

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
            writer.writerow({'date': row[0], 'new_cases': row[5]})
getData("data", stateInitials )
