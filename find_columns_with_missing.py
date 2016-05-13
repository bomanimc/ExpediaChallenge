with open("booking_only.csv", "r") as rf:
  with open("booking_no_empty.csv", "w") as wf:
    headers = rf.readline()
    headers = headers.split(',')
    del headers[6]
    headercount = [0]*len(headers)
    for line in rf:
      print "..."
      splitline = line.split(',')
      for idx, item in enumerate(splitline):
        if item == "" or item == "?":
          headercount[idx] = headercount[idx] + 1

  for i in range(len(headers)):
    print headers[i], headercount[i]
