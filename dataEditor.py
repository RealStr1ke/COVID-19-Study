import os
import csv
import wget
import pandas as pd


dataCDC = './assets/cases.csv'
stateInitials = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK", "OR", "PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
stateInitialsL = ["al","ak","az","ar","ca","co","ct","de","fl","ga","hi","id","il","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","ok", "or", "pa","pr","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy"]
stateNames=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
def getData(folder, names, initials):
  # if os.path.exists(dataCDC):
  #   os.remove(dataCDC)
  # print('Retrieving CDC data...')
  # url = 'https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD'
  # wget.download(url, './src/cases.csv')
  # print('Retrieved CDC data.')

  # csvCDC = csv.reader(dataCDC)
  # for row in csvCDC:
  #   row[0] = (str(row[0])).replace("/", "-")
  # cdcData = pd.read_csv("./assets/cases.csv")
  # cdcData['submission_date'] = pd.to_datetime(cdcData.submission_date, infer_datetime_format = True)
  # cdcData.sort_values(by = 'submission_date', ascending = True, inplace = True)
  
  # download-directory.github.io?url=https://github.com/{org/user}/{repo}/tree/{branch}/{path}

  iNum = 0
  sNum = 0

  for initial in initials:
    file = initials +"_cases.csv"
    filePath = os.path.join("/" + folder, file)
    if os.path.exists(filePath):
      os.remove(filePath)
    print(file)
    newFile = open(file, "w")
    newFilePath = "./" + folder + "/" + file
    os.rename("./" + file, newFilePath)
    with open(newFilePath, mode='w') as data:
      headers = ['Date', 'New Cases']
      writer = csv.DictWriter(data, fieldnames=headers)

      writer.writeheader()
      with open(dataCDC, mode='r') as cases:
        reader = csv.reader(cases)
        for row in reader:
          if row[1].lower() == names:
            writer.writerow({'Date': row[0], 'New Cases': row[5]})
    iNum = iNum + 1;
    sNum = sNum + 1;

getData("data", stateNames, stateInitialsL)
