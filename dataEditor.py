import os
import csv
import wget
from glob import glob
import pandas as pd
import shutil

dirJHU = './data/raw/'

stateInitials = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK", "OR", "PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
stateInitialsL = ["al","ak","az","ar","ca","co","ct","de","fl","ga","hi","id","il","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","ok", "or", "pa","pr","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy"]
stateNames=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
def getData(folder, names, initials):
  # print('Clearing raw JHU data...\n')
  # shutil.rmtree(dirJHU)
  # print('Cleared raw JHU data.\n')

  # print('Clearing COVID-19 data...\n')
  # shutil.rmtree("./" + folder + "/")
  # print('Cleared COVID-19 data.\n')
  os.makedirs(folder, exist_ok=True)

  rawFiles = [glob('./data/raw/*.csv')]
  initNum = 0
  print('Creating state data files...')
  for init in initials:
    sFile = init +"_cases.csv"
    sPath = os.path.join("./" + folder, sFile)
    if os.path.exists(sPath):
      os.remove(sPath)
    newFile = open(sPath, "w")
    headers = ['Date', 'New Cases']
    writer = csv.DictWriter(newFile, fieldnames=headers)
    writer.writeheader()
    # newFilePath = "./" + folder + "/" + file
    # os.rename("./" + file, newFilePath)
    # print(names[initNum])
    initNum = initNum + 1
  print('Created state data files...')

  for rFile in rawFiles:
    # print(rFile)
    rawFile = csv.reader(rFile)
    for row in rawFile:
      sNum = 0
      print('Reading row #' + str(sNum))
      for name in names:
        if row[0] == name:
          print('True')
          headers = ['Date', 'New Cases']
          writer = csv.DictWriter(os.path.join("./" + folder, initials[sNum]), fieldnames=headers)
          writer.writerow({'Date': rFile, 'New Cases': row[5]})
          break
        else:
          sNum = sNum + 1;
  
  # for initial in initials:
  #   file = initial +"_cases.csv"
  #   with open(newFilePath, mode='w') as data:
  #     headers = ['Date', 'New Cases']
  #     writer = csv.DictWriter(data, fieldnames=headers)
  #     writer.writeheader()

  #     for filename in os.listdir(dataJHU):
  #       if filename.endswith(".csv"):
  #         cFile = os.path.join(dataJHU, filename)
  #         with open(cFile, mode='r') as curFile:
  #           print(cFile)
  #           reader = csv.reader(curFile)
  #           iNum = 0
  #           for row in reader:
  #             for sName in stateNames:
  #               if row[0] == sName:
  #                 with open(file, mode='w') as stateFile:
  #                   writer = csv.DictWriter(stateFile, fieldnames=headers)
  #                   writer.writerow({'Date': filename.replace('.csv', "", 1), 'New Cases': row[5]})
  #       else:
  #         continue
getData("dataset", stateNames, stateInitialsL)
