with open("/Users/dianeliu/Downloads/train.csv", "r") as rf:
  count = 1
  headers = rf.readline()
  headers = headers.split(',')
  headercount = [0]*len(headers)
  for line in rf:
    splitline = line.split(',')
    for idx, item in enumerate(splitline):
      if item == "" or item == "?":
        headercount[idx] = headercount[idx] + 1

  for i in range(len(headers)):
    print headers[i], headercount[i]
    
print count