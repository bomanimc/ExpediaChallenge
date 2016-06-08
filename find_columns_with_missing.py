<<<<<<< HEAD
with open("/Users/dianeliu/Downloads/train.csv", "r") as rf:
  count = 1
=======
with open("/Users/dianeliu/Code/ExpediaChallenge/booking_only.csv", 'r') as rf:
>>>>>>> e998543c6e07664e61efaf9fd8c2d3f5d170c46b
  headers = rf.readline()
  headers = headers.split(',')
  headercount = [0]*len(headers)
  for line in rf:
<<<<<<< HEAD
=======
    print "..."
>>>>>>> e998543c6e07664e61efaf9fd8c2d3f5d170c46b
    splitline = line.split(',')
    for idx, item in enumerate(splitline):
      if item == "" or item == "?":
        headercount[idx] = headercount[idx] + 1

  for i in range(len(headers)):
    print headers[i], headercount[i]
<<<<<<< HEAD
    
print count
=======
>>>>>>> e998543c6e07664e61efaf9fd8c2d3f5d170c46b
