count = 0

with open("/Users/dianeliu/Downloads/train.csv", 'r') as rf:
  with open("/Users/dianeliu/Code/ExpediaChallenge/booking_only.csv", 'w') as wf:
    wf.write(rf.readline())
    for line in rf:
      splitline = line.split(',')
      if splitline[18] == "1":
        wf.write(line)
        count = count + 1
        print "wrote", count, "line"