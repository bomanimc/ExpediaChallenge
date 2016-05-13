with open("booking_only.csv", "r") as rf:
  with open("booking_no_empty.csv", "w") as wf:
    headers = rf.readline()
    headers = headers.split(',')
    del headers[6]
    headers = ','.join(headers)
    wf.write(headers)
    for line in rf:
        line = line.split(',')
        del line[6]
        line = ','.join(line)
        wf.write(line)
        
print "DONE"